from app.MLModel.MLModel import MLModel
import os

from pandas.io.parsers import read_csv
from app.Observers.Mail_Observers.Mail_Observer import Mail_Observer
from django.test import TestCase
# Method create tag mapping
class Test_Method_Update_Observers(TestCase):
    pass
    def test0(self):
        """Test : Test Tag Mapping"""
        filename =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'train.csv')
        mapping_csv = read_csv(filename)
        mlmodel=MLModel()
        result=mlmodel.create_tag_mapping(mapping_csv)
        print(result)
        self.assertIsNone(result)
