from app.Helpers.Auth_Helper import generate_password, generate_token, send_password_to
from django.test import TestCase
from app.Models.Users import Users
# Method Generate Password
class Test_Method_Generate_password(TestCase):
    pass
    # def test0(self):
    #     """Test : Check Generate Password Method"""
    #     password=generate_password()
    #     self.assertIsInstance(password,str)
    #     self.assertTrue(len(password)==12)

# Method Generate Token
class Test_Method_Generate_Token(TestCase):
    pass
    # def test1(self):
    #     """Test : Check Generate Token Method"""
    #     token=generate_token()
    #     self.assertIsInstance(token,dict)
    #     self.assertTrue('value' in token.keys())
    #     self.assertTrue('isvalid' in token.keys())
    #     self.assertTrue('generated_time' in token.keys())
    #     self.assertTrue(len(token['value'])==25)
# Method Send Email
class Test_Method_Send_Email(TestCase):
    pass
    # def test2(self):
    #     """Test : Check Send Email Method All Valid"""
    #     user=Users()
    #     user.set_user_email('mashkarharis3@gmail.com')
    #     email_sent=send_password_to(user,'wrr4gbtefvr')
    #     self.assertIsNone(email_sent)
    # def test3(self):
    #     """Test : Check Send Email Method InvalidEmail"""
    #     user=Users()
    #     user.set_user_email(None)
    #     email_sent=send_password_to(user,'wrr4gbtefvr')
    #     self.assertIsNone(email_sent)
    # def test4(self):
    #     """Test : Check Send Email Method Invalid Password"""
    #     user=Users()
    #     user.set_user_email('mashkarharis3@gmail.com')
    #     email_sent=send_password_to(user,None)
    #     self.assertIsNone(email_sent)
           