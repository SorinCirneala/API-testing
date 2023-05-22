import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import utils.api_actions as api

def test_api_is_up():
    response = api.get_status()
    assert response.status_code == 200
    assert response.json()["status"] == "UP"
