from app.Reports.Report import Report



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
        return "OK"
        