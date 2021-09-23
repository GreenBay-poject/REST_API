from app.Reports.Generate_Report import Generate_Report
from app.Reports.Report import Report
from io import BytesIO
import requests
from PIL import Image
import matplotlib.pyplot as plt

class LandReport(Report):
    
    url=None
    
    def __init__(self,mlmodel):
        super(self.__class__, self).__init__(mlmodel)
    
    def set_urls(self, urls_array):
        self.url=urls_array[0]
    
    def generate_report(self):
        print("I am Generating Land Report")
        
        # load the image
        response = requests.get(self.url)
        report,tile_tags=Generate_Report(response,super())
        return [report,tile_tags] #super().getModel().get_prediction(img)
        