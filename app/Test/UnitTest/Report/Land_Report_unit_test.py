from app.MLModel.MLModel import MLModel
from app.Reports.DeforestationReport import DeforestationReport
from app.Report_Factory.FacoryValues import DEFORESTATION_REPORT, LAND_REPORT
from app.Reports.LandReport import LandReport
from app.Report_Factory.ReportFactory import ReportFactory
from django.test import TestCase
# Method Generate Report
class Test_Method_Generate_Report(TestCase):
    pass
    # def test0(self):
    #     """Test : Generate Report for Valid Url"""
    #     mlmodel=MLModel()
    #     land_report=LandReport(mlmodel)
    #     land_report.set_urls(['https://openforests.com/wp-content/uploads/2018/02/sat.png'])
    #     result=land_report.generate_report()
    #     analyze=result[0]
    #     content=result[1]

    #     self.assertIsInstance(analyze,dict)
    #     self.assertTrue(len(analyze)>0)

    #     self.assertIsInstance(content,list)
    #     self.assertTrue(len(content)>0)
    #     self.assertIsInstance(content[0],list)

    # def test1(self):
    #     """Test : Generate Report for Invalid Url"""
    #     mlmodel=MLModel()
    #     land_report=LandReport(mlmodel)
    #     with self.assertRaises(Exception):
    #         land_report.set_urls(['https://openforests.comm/wp-content/uploads/2018/02/sat.png'])
    #         result=land_report.generate_report()
       