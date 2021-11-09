import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
import json

class GetUserInfo(APITestCase):

    def test_guser_regster(self):
        """
        Both Valid Uname and Email
        """
        # Data
        url = '/auth/login'
        data ={
            "email": "mashkarharis3@gmail.com",
            "password": "ABC123"
        }
        # Send Request
        response = self.client.post(url, data=data, format='json')
        # Status Code Check
        print(response.__dict__)
        print(type(response.__dict__["_container"]))
        print(response.__dict__["_container"])
        print(response.__dict__["_container"][0][5:])
        print(type(response.__dict__["_container"][0][5:]))
        self.assertContains(response, 'Token')
        print(response.body)
        # self.assertEqual(response.UserEmail, "mashkarharis3@gmail.com")
        self.assertEqual(response.status_code, status.HTTP_200_OK)