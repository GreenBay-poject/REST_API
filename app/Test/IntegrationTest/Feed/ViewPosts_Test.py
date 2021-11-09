import json
from rest_framework import status
from rest_framework.test import APITestCase


class GetDates_Test(APITestCase):
    def test_in_range_lat_lon(self):
        """
        Personal Posts
        """
        # Prepare Url
        url = '/feed/view_posts'
        # Send Request
        response = self.client.get(url, None, format='json')
        # Status Code Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Field Contain Check
        self.assertContains(response,'ALL_POSTS')