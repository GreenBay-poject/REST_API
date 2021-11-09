import json
from rest_framework import status
from rest_framework.test import APITestCase

class GetDates_Test(APITestCase):
    def test_in_range_lat_lon(self):
        """
        Delete Post
        """
        # Prepare Url
        url = '/feed/delete_post'
        data={
            "email": "mashkarharis3@gmail.com",
            "post_id": 1634868985679
        }
        # Send Request
        response = self.client.post(url, data=data, format='json')
        # Status Code Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Field Contain Check
        # self.assertContains(response,'All_Dates_Available')
        # # Properties of Field Check
        # json_body=response.json()
        # # print(json_body)
        # self.assertTrue(len(json_body['All_Dates_Available'])>0)