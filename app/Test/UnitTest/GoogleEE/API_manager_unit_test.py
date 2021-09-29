from app.GoogleEE.APIManager import APIManager
from django.test import TestCase

# Method Initialize
class Test_Method_Initialize(TestCase):
    pass
    def test0(self):
        """Test : Check Whther GoogleEE initialize with no error"""
        api_manager=APIManager()
        result=api_manager.initialize()
        self.assertIsNone(result)

# Method Get Available Dates
class Test_Method_Get_Available_Dates(TestCase):
    pass
    def test1(self):
        """Test : Check For valid lat and lon"""
        api_manager=APIManager()
        api_manager.initialize()
        result=api_manager.get_available_dates(80.78,23.56)
        self.assertIsInstance(result,list)
        self.assertTrue(len(result)>0)
    def test2(self):
        """Test : Check For No latitude given"""
        api_manager=APIManager()
        api_manager.initialize()
        with self.assertRaises(Exception):
            api_manager.get_available_dates(None,23.56)
    def test3(self):
        """Test : Check For No longitude given"""
        api_manager=APIManager()
        api_manager.initialize()
        with self.assertRaises(Exception):
            api_manager.get_available_dates(23.56,None)

    def test4(self):
        """Test : Check For valid Out of range latitude"""
        api_manager=APIManager()
        api_manager.initialize()
        result=api_manager.get_available_dates(8000.78,23.56)
        print(result)
        self.assertIsInstance(result,list)
        self.assertTrue(len(result)>0)
    def test5(self):
        """Test : Check For valid Out of range longitude"""
        api_manager=APIManager()
        api_manager.initialize()
        result=api_manager.get_available_dates(80.78,-22321.56)
        print(result)
        self.assertIsInstance(result,list)
        self.assertTrue(len(result)>0)

    def test6(self):
        """Test : Check For string latitude"""
        api_manager=APIManager()
        api_manager.initialize()
        
        with self.assertRaises(Exception):
            result=api_manager.get_available_dates("8000",23.56)
    
    def test7(self):
        """Test : Check For string longitude"""
        api_manager=APIManager()
        api_manager.initialize()
        
        with self.assertRaises(Exception):
            result=api_manager.get_available_dates(80,"23.56")

# Method Fetch Image
class Test_Method_Fetch_Image(TestCase):
    pass
    def test8(self):
        """Test : Check For Fetch Image for unavailable date"""
        api_manager=APIManager()
        api_manager.initialize()
        with self.assertRaises(Exception):
            result=api_manager.fetch_image(80.78,23.56,'2018-12-17')
        

    def test9(self):
        """Test : Check For Fetch Image for available date"""
        api_manager=APIManager()
        api_manager.initialize()
        result=api_manager.fetch_image(6.177856842841487,80.2139575381279,'2018-12-17')
        self.assertIsNotNone(result)
