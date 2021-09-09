from app.Reports.Report import Report



class LandReport(Report):
    
    url=None
    
    def __init__(self,mlmodel):
        super(self.__class__, self).__init__(mlmodel)
    
    def set_urls(self, urls_array):
        self.url=urls_array[0]
    
    def generate_report(self):
        print("I am Generating Land Report")
        return super().getModel().get_prediction(self.url)
        