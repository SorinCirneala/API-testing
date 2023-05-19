import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import requests
from requests import Response
from utils.endpoints import carts_url, carts_url, orders_url, products_url, register_url, status_url

def get_status() -> Response:
    response = requests.get(status_url)
    return response