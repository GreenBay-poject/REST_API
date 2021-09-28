from app.Helpers.QnAHelpers import send_answer_added_email
from app.Helpers.Auth_Helper import generate_password, generate_token, send_password_to
from django.test import TestCase
from app.Models.Users import Users
# Method send_answer_added_email
class Test_Method_send_answer_added_email(TestCase):
    pass
    # def test0(self):
    #     """Test : Check Send Email With Valid Post"""
    #     result=send_answer_added_email('mashkarharis3@gmail.com','Sample Title','Sample Description','Sample Answer','ASHKAR MHM')
    #     self.assertIsNone(result)
    # def test1(self):
    #     """Test : Check Send Email With no title"""
    #     with self.assertRaises(Exception):
    #         result=send_answer_added_email('mashkarharis3@gmail.com',None,'Sample Description','Sample Answer','ASHKAR MHM')
    # def test2(self):
    #     """Test : Check Send Email With no description"""
    #     with self.assertRaises(Exception):
    #         result=send_answer_added_email('mashkarharis3@gmail.com','Sample Title',None,'Sample Answer','ASHKAR MHM')
    # def test3(self):
    #     """Test : Check Send Email With no answer"""
    #     with self.assertRaises(Exception):
    #         result=send_answer_added_email('mashkarharis3@gmail.com','Sample Title','Sample Description',None,'ASHKAR MHM')
    # def test4(self):
    #     """Test : Check Send Email With no sendername"""
    #     with self.assertRaises(Exception):
    #         result=send_answer_added_email('mashkarharis3@gmail.com','Sample Title','Sample Description','Sample Answer',None)
          
