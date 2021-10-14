from io import BytesIO
from PIL import Image
from keras.preprocessing.image import load_img
import numpy
import requests
from app.MLModel.MLModel import MLModel
import os

from pandas.io.parsers import read_csv
from app.Observers.Mail_Observers.Mail_Observer import Mail_Observer
from django.test import TestCase

# Method create tag mapping
class Test_Method_Tag_Mapping(TestCase):
    pass
    def test0(self):
        """Test : Test Tag Mapping"""
        filename =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'train.csv')
        mapping_csv = read_csv(filename)
        mlmodel=MLModel()
        result=mlmodel.create_tag_mapping(mapping_csv)
        self.assertTrue(result!=None)
        self.assertIsInstance(result,tuple)
        self.assertIsInstance(result[0],dict)
        self.assertIsInstance(result[1],dict)
        self.assertTrue(len(result)==2)
        self.assertTrue(len(result[0])==17)
        self.assertTrue(len(result[1])==17)

# Method prediction to tags
class Test_Method_prediction_to_tags(TestCase):
    pass
    def test0(self):
        """Test : Test Prediction to tag"""

        mlmodel=MLModel()
        # load the mapping file 
        filename =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'train.csv')
        # Read CSV
        mapping_csv = read_csv(filename)
        # create a mapping of tags to integers
        _, inv_mapping = mlmodel.create_tag_mapping(mapping_csv)
        prediction=numpy.array([0.23,0.12,0.56,0.73,0.78,0.98,0.81,0.99,0.12,0.99,0.61,1,0.11,0.29,0.41,0.68,0.13])
        tags=mlmodel.prediction_to_tags(inv_mapping,prediction)
        self.assertIsNotNone(tags)
        self.assertIsInstance(tags,list)

# Method Load Image
class Test_Method_Load_Image(TestCase):
    pass
    def test0(self):
        """Test : Test Load Image"""
        response = requests.get('https://openforests.com/wp-content/uploads/2018/02/sat.png')
        img_bytes = BytesIO(response.content)
        img = Image.open(img_bytes)
        mlmodel=MLModel()
        result=mlmodel.load_image(img)
        self.assertIsNotNone(result)

# Method RunModel
class Test_Method_RunModel(TestCase):
    pass
    def test0(self):
        """Test : Test Run Model"""
        response = requests.get('https://openforests.com/wp-content/uploads/2018/02/sat.png')
        img_bytes = BytesIO(response.content)
        img = Image.open(img_bytes)
        
        mlmodel=MLModel()
        filename =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'train.csv')
        mapping_csv = read_csv(filename)
        _, inv_mapping = mlmodel.create_tag_mapping(mapping_csv)
        
        
        result=mlmodel.run_model(inv_mapping,img)

        print(result)

        self.assertIsNotNone(result)
        self.assertIsInstance(result,list)


# Method Get Prediction
class Test_Method_Get_Prediction(TestCase):
    pass
    def test0(self):
        """Test : Test Get Prediction"""
        response = requests.get('https://openforests.com/wp-content/uploads/2018/02/sat.png')
        img_bytes = BytesIO(response.content)
        img = Image.open(img_bytes)
        
        mlmodel=MLModel()
        
        result=mlmodel.get_prediction(img)

        print(result)

        self.assertIsNotNone(result)
        self.assertIsInstance(result,list)