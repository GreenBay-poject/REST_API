import json
from rest_framework import status
from rest_framework.test import APITestCase


class GetDates_Test(APITestCase):
    def test_add_post(self):
        """
        Add Post
        """
        # Prepare Url
        url = '/feed/add_post'
        data={
            "email":"mashkarharis3@gmail.com",
            "title":"Calves and kittens and snakelets, oh my! OKC Zoo family grows with significant births",
            "description":"Kioni is just one of several new additions to the OKC Zoo family, which has recently welcomed a rare clouded leopard kitten, three Eastern massasauga snakelets and four black tree monitor hatchlings, as well as two adult bat-eared foxes. Another giraffe calf is expected soon, as well as an Asian elephant calf due in February.Our animal family is always growing, said Candice Rennels, zoo director of public relations. It is very exciting that there are so many right now and that they're all so diverse in species. ... These new births are ambassadors for their species as a whole and are really contributing to the longevity of their populations",
            "image_url":"https://cdn.pixabay.com/photo/2019/10/23/06/30/hamburg-4570577__340.jpg"
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