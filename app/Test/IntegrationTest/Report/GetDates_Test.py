import json
from rest_framework import status
from rest_framework.test import APITestCase


class GetDates_Test(APITestCase):
    def test_in_range_lat_lon(self):
        """
        Both Valid Latitude and Longitude
        """
        # Prepare Url
        url = '/report/get_dates?lattitude=6.177856842841487&longitude=80.2139575381279'
        # Send Request
        response = self.client.get(url, None, format='json')
        # Status Code Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Field Contain Check
        self.assertContains(response,'All_Dates_Available')
        # Properties of Field Check
        json_body=response.json()
        # print(json_body)
        self.assertTrue(len(json_body['All_Dates_Available'])>0)