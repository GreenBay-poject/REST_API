import ee
from back_end_rest_api.settings import SERVICE_ACCOUNT_GEE


class APIManager:
    
    def initialize(self):
        credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT_GEE, 'privatekey.json')
        ee.Initialize(credentials)
    
    def get_available_dates(self,lattitude,longitude):
        landsat = ee.ImageCollection("COPERNICUS/S2_SR")
        gap=0.015
        Ituna_AOI = ee.Geometry.Rectangle([longitude,lattitude,longitude+gap,lattitude+gap])
        landsat_AOI = landsat.filterBounds(Ituna_AOI)
        #print(landsat_AOI.first().bandNames().getInfo())
        landsat_AOI=landsat_AOI#.sort('CLOUD_COVER')
        date_list=landsat_AOI.aggregate_array('system:time_start').getInfo()
        print(date_list)
        return date_list
        
