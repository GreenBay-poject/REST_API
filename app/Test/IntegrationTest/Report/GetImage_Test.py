import json
from rest_framework import status
from rest_framework.test import APITestCase


class GetDates_Test(APITestCase):
    def test_in_range_lat_lon(self):
        """
        Both Valid Latitude and Longitude
        """
        # Prepare Url
        url = '/report/get_image?lattitude=6.177856842841487&longitude=80.2139575381279&date=2018-12-22'
        # Send Request
        response = self.client.get(url, None, format='json')
        # Status Code Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Field Contain Check
        self.assertContains(response,'Image')
        # self.assertTrue('DateTIme' in Image.keys())
        # self.assertTrue('Url' in Image.keys())
        json_body=response.json()
        # data= json_body.get("data")[0]
        # # print(json_body)
        # self.assertTrue('DateTime' in data.get("values")[0])

class GetDates_Test_Withouth_long(APITestCase):
    def test_in_range_lat_lon(self):
        """
        Both Valid Latitude and Longitude
        """
        # Prepare Url
        url = '/report/get_image?lattitude=6.177856842841487&date=2018-12-22'
        # Send Request
        response = self.client.get(url, None, format='json')
        # Status Code Check
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Field Contain Check
        # self.assertContains(response,'DateTime')
        # self.assertContains(response, 'url')
        # Properties of Field Check
        json_body=response.json()
        # print(json_body)
        # self.assertTrue(len(json_body['image'])>0)