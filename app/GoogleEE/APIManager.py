import ee
from back_end_rest_api.settings import SERVICE_ACCOUNT_GEE
import os
from datetime import datetime as dt
from app.Models.UrlImage import UrlImage


class APIManager:
    
    def initialize(self):
        # Join Path
        path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'privatekey.json')
        # Print Path
        # print(path)
        # Create Credentials Object 
        credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT_GEE, path)
        # Initialize EE
        ee.Initialize(credentials)
    
    def get_available_dates(self,lattitude,longitude):
        # Choose Satellite
        landsat = ee.ImageCollection("COPERNICUS/S2_SR")
        # Gap Between Latitude and Longitude
        gap=0.015
        # Choose Rectangular Area
        Ituna_AOI = ee.Geometry.Rectangle([longitude,lattitude,longitude+gap,lattitude+gap])
        # Put rectangle as bound
        landsat_AOI = landsat.filterBounds(Ituna_AOI)
        #print(landsat_AOI.first().bandNames().getInfo())
        # Sort by cloud coverage
        landsat_AOI=landsat_AOI#.sort('CLOUD_COVER')
        # Get dates
        date_list=landsat_AOI.aggregate_array('system:time_start').getInfo()
        #print(date_list)
        # Return Dates
        return date_list
    
    def fetch_image(self, lattitude, longitude, date):
        # Choose Satellite
        landsat = ee.ImageCollection("COPERNICUS/S2_SR")
        # Gap between Lat and Long
        gap=0.015
        # Choose Rectangular Area
        Ituna_AOI = ee.Geometry.Rectangle([longitude,lattitude,longitude+gap,lattitude+gap])
        # Put Rectangle as Bound
        landsat_AOI = landsat.filterBounds(Ituna_AOI)
        # Required Dates
        date_input=ee.Date(str(date))
        date_1=date_input.advance(-1, 'day')
        date_2=date_input.advance(1, 'day')
        # Filter by Date
        landsat_AOI = landsat_AOI.filterDate(date_1, date_2) 
        # Sort By Cloud Coverage
        landsat_AOI=landsat_AOI.sort('CLOUD_COVER')
        # Get Image With Least Cloud Coverage
        least_cloudy = ee.Image(landsat_AOI.first())
        # Get Cloud Coverage
        cloud_coverage=least_cloudy.get('CLOUD_COVER').getInfo()
        # Get Date
        image_date_epoch = ee.Date(least_cloudy.get('system:time_start'))
        time = image_date_epoch.getInfo()['value']/1000.
        image_date_prepared=dt.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        # Get Url
        parameters = {
            'min': 0,
            'max': 2000,
            'dimensions': 400,
            'bands': ['B4', 'B3', 'B2'],
            #"scale":3,
            'region': Ituna_AOI
        }
        url = least_cloudy.getThumbUrl(parameters)
        # Prepare Image Object
        image=UrlImage()
        image.set_cloud_coverage(cloud_coverage)
        image.set_date_time(image_date_prepared)
        image.set_url(url)
        # Return Image
        return image        
