import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import json

def get_testdata(filename: str, test_name: str) -> list:
    """ Parses JSON file (filename) and returns the list of inputs for the specified test case (test_name) """
    file_path = os.path.join(project_path, "testdata", filename)
    with open(file_path) as fn:
        for td in json.load(fn):
            if td["tc_name"] == test_name:
                return list(td["inputs"])
