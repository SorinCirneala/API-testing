import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

from utils.api_actions import get_status

def test_api_status():
    response = get_status()
    assert response.status_code == 200