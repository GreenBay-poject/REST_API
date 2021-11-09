import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class GetUserInfo(APITestCase):

    def test_guser_regster(self):
        """
        Both Valid Uname and Email
        """
        # Data
        url = '/auth/register'
        data ={
            "name":"Mohomed Ashkar Haris",
            "email":"mashkarharis2@gmail.com",
            "age":"23",
            "address":"43/3A Galle",
            "gender":"Male",
            "postalcode":"80000",
            "position": "Director",
            "ministry_name": "Wild Life Protection Ministry",
            "secret_code": 212434
        }
        # Send Request
        response = self.client.post(url, data=data, format='json')
        # Status Code Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)