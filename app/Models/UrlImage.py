
class UrlImage:
    
    __cloud_coverage=None
    __date_time=None
    __url=None
    
    def tojson(self):
        return {
            "Cloud Coverage":self.__cloud_coverage,
            "DateTIme": self.__date_time,
            "Url":self.__url
        }

    def get_cloud_coverage(self):
        return self.__cloud_coverage


    def get_date_time(self):
        return self.__date_time


    def get_url(self):
        return self.__url


    def set_cloud_coverage(self, value):
        print(value)
        self.__cloud_coverage = value


    def set_date_time(self, value):
        self.__date_time = value


    def set_url(self, value):
        self.__url = value

    
    
    
    
    
    