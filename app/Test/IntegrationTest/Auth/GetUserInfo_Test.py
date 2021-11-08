import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

class GetUserInfo(APITestCase):
    
    def test_get_user_info(self):
        """
        Both Valid Uname and password
        """
        # Data
        data={"email": "mashkarharis3@gmail.com"}
        # Prepare Url
        url = '/auth/get_user_info'
        # Send Request
        client=APIClient()
        # Set Credintials
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + "RYPWXPWEEYZZSGNHGIQXRSYNQ")
        # Get Response
        response = client.post(url,data=data,format='json')
        # Print Response
        print(response)
        print(response.status_code)
        # # Status Code Check
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # # Field Contain Check
        # self.assertContains(response,'All_Dates_Available')
        # # Properties of Field Check
        # json_body=response.json()
        # # print(json_body)
        # self.assertTrue(len(json_body['All_Dates_Available'])>0)