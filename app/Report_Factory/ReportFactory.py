from app.Report_Factory.FacoryValues import LAND_REPORT, DEFORESTATION_REPORT
from app.MLModel.MLModel import MLModel
from app.Reports.LandReport import LandReport
from app.Reports.DeforestationReport import DeforestationReport



class ReportFactory:
    
    def create_report(self, type):
        
        if type == LAND_REPORT:
            mlmodel=MLModel()
            return LandReport(mlmodel)

        elif type == DEFORESTATION_REPORT:
            mlmodel=MLModel()
            return DeforestationReport(mlmodel)

        else:
            return None