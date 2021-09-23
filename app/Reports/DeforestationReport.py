from app.Reports.Generate_Report import Generate_Report
from app.Reports.Report import Report
from io import BytesIO
import requests
from PIL import Image
import matplotlib.pyplot as plt



class DeforestationReport(Report):
    
    url1=None
    url2=None
    
    def __init__(self,mlmodel):
        super(self.__class__, self).__init__(mlmodel)
    
    def set_urls(self, urls_array):
        self.url1=urls_array[0]
        self.url2=urls_array[1]
    
    def generate_report(self):
        print("I am Generating Deforestation Report")
        
        # load the image
        response = requests.get(self.url1)
        report_1,tile_tags_1=Generate_Report(response,super())

        # load the image
        response = requests.get(self.url2)
        report_2,tile_tags_2=Generate_Report(response,super())

        return [report_1,tile_tags_1,report_2,tile_tags_2] #super().getModel().get_prediction(img)
        