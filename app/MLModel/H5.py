from keras.models import load_model
import os

class H5:
    
    model=None

    @staticmethod
    def load_model():
        if(H5.model==None):
            model_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'final_model.h5')
            # load model
            H5.model = load_model(model_path)

        
        return H5.model