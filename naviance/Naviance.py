from enum import Enum
from typing import Dict
import requests
from naviance import config


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
    STUDENT_FILE_PATH = '/home/nathanjones/Desktop/Naviance/student-single.csv'
    PARENT_FILE_PATH = '/home/nathanjones/Desktop/Naviance/parent-single.csv'

    def import_data(self, payload: Dict[str, str], csv_data: str) -> requests.Response:
        files = {
            # file name must be 'datafile'
            'datafile': ('data.csv', csv_data)
        }

        common_payload = {
            'account': config.ACCOUNT,
            'username': config.USERNAME,
            'key': config.DATA_IMPORT_KEY,
            'format': config.IMPORT_FORMAT,
            'header': config.IMPORT_HEADER,
        }

        full_payload = {**common_payload, **payload}

        r = requests.post(config.API_URL, data=full_payload, files=files)

        return r

    def import_students(self, csv_data) -> requests.Response:
        payload = {
            'type': ImportType.STUDENT.value,
            'description': 'student_data_update'
        }

        return self.import_data(payload, csv_data)

    def import_parents(self, csv_data) -> requests.Response:
        payload = {
            'type': ImportType.PARENT.value,
            'description': 'parent_data_update'
        }

        return self.import_data(payload, csv_data)

    def import_act_scores(self, csv_data) -> requests.Response:
        payload = {
            'type': ImportType.ACT.value,
            'description': 'act_data_update'
        }

        return self.import_data(payload, csv_data)
