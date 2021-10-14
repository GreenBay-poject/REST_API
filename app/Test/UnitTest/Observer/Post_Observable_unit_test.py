from app.Observers.Posts_observable.Post_Observable import Post_Observable
from app.Observers.Mail_Observers.Mail_Observer import Mail_Observer
from django.test import TestCase
# Method Notify
class Test_Method_Notify(TestCase):
    pass
    def test0(self):
        """Test : Notify Observer with Valid Data"""
        mail_list=['mashkarharis@gmail.com','mashkarharis3@gmail.com','haris.18@cse.mrt.ac.lk']
        mail_observer=Mail_Observer(mail_list)
        message={
            'Title':'Test Title',
            'Description':'Test Description'
        }
        post_observable=Post_Observable()
        post_observable.attach(mail_observer)
        result=post_observable.notify(message)
        print(result)
        self.assertIsNone(result)

    def test1(self):
        """Test : Test Detach"""
        mail_list=['mashkarharis@gmail.com','mashkarharis3@gmail.com','haris.18@cse.mrt.ac.lk']
        mail_observer=Mail_Observer(mail_list)
        message={
            'Title':'Test Title',
            'Description':'Test Description'
        }
        post_observable=Post_Observable()
        post_observable.attach(mail_observer)
        post_observable.detach(mail_observer)
        result=post_observable.notify(message)
        print(result)
        self.assertIsNone(result)
