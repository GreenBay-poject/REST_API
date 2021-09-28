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
    #     """Test : Generate Report for Both Valid Url"""
    #     mlmodel=MLModel()
    #     land_report=DeforestationReport(mlmodel)
    #     land_report.set_urls(['https://openforests.com/wp-content/uploads/2018/02/sat.png','https://openforests.com/wp-content/uploads/2018/02/sat.png'])
    #     result=land_report.generate_report()

    #     analyze_1=result[0]
    #     content_1=result[1]

    #     analyze_2=result[2]
    #     content_2=result[3]

    #     self.assertIsInstance(analyze_1,dict)
    #     self.assertTrue(len(analyze_1)>0)

    #     self.assertIsInstance(content_1,list)
    #     self.assertTrue(len(content_1)>0)
    #     self.assertIsInstance(content_1[0],list)

    #     self.assertIsInstance(analyze_2,dict)
    #     self.assertTrue(len(analyze_2)>0)

    #     self.assertIsInstance(content_2,list)
    #     self.assertTrue(len(content_2)>0)
    #     self.assertIsInstance(content_2[0],list)

    # def test1(self):
    #     """Test : Generate Report for One Invalid Url"""
    #     mlmodel=MLModel()
    #     land_report=DeforestationReport(mlmodel)
    #     with self.assertRaises(Exception):
    #         land_report.set_urls(['https://openforests.com/wp-content/uploads/2018/02/sat.png','https://openforests.com/wpp-content/uploads/2018/02/sat.png'])
    #         result=land_report.generate_report()

    # def test2(self):
    #     """Test : Generate Report for Both Invalid Url"""
    #     mlmodel=MLModel()
    #     land_report=DeforestationReport(mlmodel)
    #     with self.assertRaises(Exception):
    #         land_report.set_urls(['https://openforests.comm/wp-content/uploads/2018/02/sat.png','https://openforests.com/wpp-content/uploads/2018/02/sat.png'])
    #         result=land_report.generate_report()
       