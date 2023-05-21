import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import requests
from requests import Response
from utils.endpoints import carts_url, carts_url, orders_url, products_url, register_url, status_url
from utils.secret import access_token

# TODO remove after debugging
from utils.secret import mock_cart_id, mock_item_id

def get_status() -> Response:
    return requests.get(status_url)


def get_all_products() -> Response:
    return requests.get(products_url)


def get_product_by_id(product_id, label=None) -> Response:
    """ 
    product_id (int)
    label (boolean)
    """
    payload = {"product-label": label}
    url = f"{products_url}/{product_id}"
    return requests.get(url, params=payload)


def create_cart() -> Response:
    return requests.post(carts_url)


def get_cart_info(cart_id) -> Response:
    """
    cart_id (string)
    """
    url = f"{carts_url}/{cart_id}"
    return requests.get(url) 


def get_cart_items(cart_id) -> Response:
    """
    cart_id (string)
    """
    url = f"{carts_url}/{cart_id}/items"
    return requests.get(url)


def add_item_to_cart(cart_id, product_id) -> Response:
    """
    cart_id (string)
    product_id (int)
    """
    url = f"{carts_url}/{cart_id}/items"
    payload = {
        "productId": str(product_id) 
    }
    return requests.post(url, json=payload)


def modify_item_in_cart(cart_id, item_id, quantity) -> Response:
    """
    cart_id (string)
    item_id (int)
    quantity (int)
    """
    url = f"{carts_url}/{cart_id}/items/{item_id}"
    payload = {
        "quantity": f"{quantity}"
    }
    return requests.patch(url, json=payload)



# TODO remove after debugging
# print(get_cart_info(mock_cart_id).text)
# response = modify_item_in_cart(mock_cart_id, mock_item_id, 3)
# print(response.text)
# print(response.request.url)
# print(response.request.body)
# print(response.request.headers)