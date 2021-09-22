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
        # Read content
        img_bytes = BytesIO(response.content)
        # Open Image
        img = Image.open(img_bytes)
        # Get img size
        w, h = img.size
        # Images
        tiles=[]
        # Split to 9 tiles
        for i in range(1,4):
            for j in range(1,4): 
                box = ((i-1)*w/3, (j-1)*h/3, i*w/3, j*h/3)
                print(box)
                # add to tiles
                tiles.append(img.crop(box))
        # showit=0
        # for image in tiles:
        #     if showit==2:
        #         image[2].show()
        #     showit+=1
        tiles[2].show()
        # tag list
        list_of_tags=[]
        tile_tags=[]
        # Return Predicted Value
        for img in tiles:
            tile_tag=[]
            tags=super().getModel().get_prediction(img)
            for tag in tags:
                list_of_tags.append(tag)
                tile_tag.append(tag)
            tile_tags.append(tile_tag)
        # Get count dict
        counts = dict()
        for i in list_of_tags:
            counts[i] = counts.get(i, 0) + 1
        # remove clear
        if 'clear' in counts.keys():
            del counts['clear']
        # Replace Primary with forest
        if 'primary' in counts.keys():
            value=counts['primary']
            del counts['primary']
            counts['forest_coverage']=value
            
        # Create Percentage dict
        sum=0
        for key in counts.keys():
            sum+=counts[key]
        report=dict()
        for key in counts.keys():
            report[key]=round((counts[key]/float(sum))*100,2)
        # return tag list
        return [report,tile_tags] #super().getModel().get_prediction(img)
        