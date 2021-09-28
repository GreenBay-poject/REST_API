from app.Reports.DeforestationReport import DeforestationReport
from app.Report_Factory.FacoryValues import DEFORESTATION_REPORT, LAND_REPORT
from app.Reports.LandReport import LandReport
from app.Report_Factory.ReportFactory import ReportFactory
from app.Helpers.QnAHelpers import send_answer_added_email
from app.Helpers.Auth_Helper import generate_password, generate_token, send_password_to
from django.test import TestCase
from app.Models.Users import Users
# Method Report Factory
class Test_Method_Report_Factory(TestCase):
    pass
    # def test0(self):
    #     """Test : Check Report Factory for Land Report"""
    #     report_factory=ReportFactory()
    #     report=report_factory.create_report(LAND_REPORT)
    #     self.assertIsInstance(report,LandReport)
    # def test1(self):
    #     """Test : Check Report Factory for Deforestation Report"""
    #     report_factory=ReportFactory()
    #     report=report_factory.create_report(DEFORESTATION_REPORT)
    #     self.assertIsInstance(report,DeforestationReport)
    # def test2(self):
    #     """Test : Check Report Factory for None Type"""
    #     report_factory=ReportFactory()
    #     report=report_factory.create_report(None)
    #     self.assertIsNone(report)
    # def test3(self):
    #     """Test : Check Report Factory for Other Type"""
    #     report_factory=ReportFactory()
    #     report=report_factory.create_report(1341)
    #     self.assertIsNone(report)