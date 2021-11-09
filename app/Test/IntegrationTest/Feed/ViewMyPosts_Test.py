import json
from rest_framework import status
from rest_framework.test import APITestCase


class GetDates_Test(APITestCase):
    def test_in_range_lat_lon(self):
        """
        Personal Posts
        """
        data = {"email": "mashkarharis3@gmail.com"}
        # Prepare Url
        url = '/feed/view_my_posts'
        # Send Request
        response = self.client.post(url, data=data, format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


