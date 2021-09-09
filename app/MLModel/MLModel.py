# make a prediction for a new image
from pandas import read_csv
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from io import BytesIO
import requests
from PIL import Image
import os

class MLModel:
    
    def printMe(self):
        print("I am OK")
    # create a mapping of tags to integers given the loaded mapping file
    def create_tag_mapping(self,mapping_csv):
        # create a set of all known tags
        labels = set()
        for i in range(len(mapping_csv)):
            # convert spaced separated tags into an array of tags
            tags = mapping_csv['tags'][i].split(' ')
            # add tags to the set of known labels
            labels.update(tags)
        # convert set of labels to a list to list
        labels = list(labels)
        # order set alphabetically
        labels.sort()
        # dict that maps labels to integers, and the reverse
        labels_map = {labels[i]:i for i in range(len(labels))}
        inv_labels_map = {i:labels[i] for i in range(len(labels))}
        return labels_map, inv_labels_map

    # convert a prediction to tags
    def prediction_to_tags(self,inv_mapping, prediction):
        # round probabilities to {0, 1}
        values = prediction.round()
        # collect all predicted tags
        tags = [inv_mapping[i] for i in range(len(values)) if values[i] == 1.0]
        return tags
    
    # load and prepare the image
    def load_image(self,filename):
        # load the image
        response = requests.get(filename)
        # Read content
        img_bytes = BytesIO(response.content)
        # Open Image
        img = Image.open(img_bytes)
        # Convert Image to RGB
        img = img.convert('RGB')
        # Resize image
        img = img.resize((96,96), Image.NEAREST)
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 96, 96, 3)
        # center pixel data
        img = img.astype('float32')
        # Filter
        img = img - [123.68, 116.779, 103.939]
        return img

    # load an image and predict the class
    def run_model(self,inv_mapping,url):
        # load the image
        img = self.load_image(url)
        # Path to model
        model_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'final_model.h5')
        # load model
        model = load_model(model_path)
        # predict the class
        result = model.predict(img)
        # map prediction to tags
        tags = self.prediction_to_tags(inv_mapping, result[0])
        # return result
        return [result[0],tags]

    def get_prediction(self,url):
        # load the mapping file 
        filename =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'train.csv')
        # Read CSV
        mapping_csv = read_csv(filename)
        # create a mapping of tags to integers
        _, inv_mapping = self.create_tag_mapping(mapping_csv)
        # entry point, run the example
        return self.run_model(inv_mapping,url)
        
        
        