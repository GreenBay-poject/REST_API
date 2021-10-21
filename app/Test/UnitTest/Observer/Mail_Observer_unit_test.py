from app.Observers.Mail_Observers.Mail_Observer import Mail_Observer
from django.test import TestCase
# Method Update Observers
class Test_Method_Update_Observers(TestCase):
    pass
    def test0(self):
        """Test : Update Observers with Valid Data"""
        mail_list=['mashkarharis@gmail.com','mashkarharis3@gmail.com','haris.18@cse.mrt.ac.lk']
        mail_observer=Mail_Observer(mail_list)
        message={
            'Title':'Test Title',
            'Description':'Test Description'
        }
        result=mail_observer.update(message)
        self.assertIsNone(result)

    def test1(self):
        """Test : Update Observers with empty mail list"""
        mail_list=[]#['mashkarharis@gmail.com','mashkarharis3@gmail.com','haris.18@cse.mrt.ac.lk']
        mail_observer=Mail_Observer(mail_list)
        message={
            'Title':'Test Title',
            'Description':'Test Description'
        }
        result=mail_observer.update(message)
        self.assertIsNone(result)
