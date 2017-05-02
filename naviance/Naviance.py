from enum import Enum
from typing import Dict
import requests


class ImportType(Enum):
    """
    Import types can be found in the School Guide to Importing and Exporting Data 2017 document
    """

    STUDENT = 1
    PARENT = 12
    SAT_BEFORE_MAR_2016 = 5
    SAT = 39
    PSAT_BEFORE_OCT_2015 = 6
    PSAT = 29
    ACT_BEFORE_OCT_2015 = 7
    ACT = 28
    PLAN = 8
    EXPLORE = 17
    SAT_SUBJECT = 9
    AP = 10
    STATE_EXAM_SCORES_MULTIPLE = 23
    STATE_EXAM_SCORE_SINGLE = 24
    STUDENT_COURSE = 33


class Naviance(object):
    def __init__(self,
                 account: str,
                 username: str,
                 email: str,
                 data_import_key: str,
                 has_header: bool,
                 import_format: str = 'csv',
                 api_url: str = 'https://services.naviance.com/district_import.php') -> None:
        """
        Creates a Naviance client object that can be used to send data files to Naviance SchoolSync

        :param acccount: str, Account you use to login to Naviance (not to be confused with Username)
        :param username: str, Naviance Username
        :param email: str, Email Address that Naviance will send import reports to
        :param data_import_key: str, Naviance Data Import Key. Can be found on the Data Import Page in the Naviance District interface
        :param has_header: bool, True if the first line of your csv file is a header row, False if it is not
        :param import_format: str
        """

        self.account = account
        self.username = username
        self.email = email
        self.data_import_key = data_import_key
        self.has_header = has_header
        self.import_format = import_format
        self.api_url = api_url

    def import_data(self, payload: Dict[str, str], raw_import_data: str) -> requests.Response:
        """
        A general-purpose function for sending import data to SchoolSync

        :param payload: Dict[str, str], POST request body
        :param raw_import_data: str, csv representation of the data that will be sent to SchoolSync as a multipart-encoded binary file
        """

        files = {
            # file name field must be 'datafile'
            'datafile': ('data.csv', raw_import_data)
        }

        common_payload = {
            'account': self.account,
            'username': self.username,
            'key': self.data_import_key,
            'format': self.import_format,
            'header': 'Yes' if self.has_header is True else 'No',
        }

        full_payload = {**common_payload, **payload}

        resp = requests.post(self.api_url, data=full_payload, files=files)

        return resp

    def import_students(self, raw_import_data: str) -> requests.Response:
        """
        Perform an import of Student data
        """
        payload = {
            'type': ImportType.STUDENT.value,
            'description': 'student_data_update'
        }

        return self.import_data(payload, raw_import_data)

    def import_parents(self, raw_import_data: str) -> requests.Response:
        """
        Perform an import of Parent data
        """
        payload = {
            'type': ImportType.PARENT.value,
            'description': 'parent_data_update'
        }

        return self.import_data(payload, raw_import_data)

    def import_act_scores(self, raw_import_data: str) -> requests.Response:
        """
        Perform an import of ACT test scores
        """

        payload = {
            'type': ImportType.ACT.value,
            'description': 'act_data_update'
        }

        return self.import_data(payload, raw_import_data)

    def import_student_course(self, raw_import_data: str) -> requests.Response:
        """
        Perform an import of Student Course data
        """

        payload = {
            'type': ImportType.STUDENT_COURSE.value,
            'description': 'student_course_update'
        }

        return self.import_data(payload, raw_import_data)
