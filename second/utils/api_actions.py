import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import requests
from requests import Response
from utils.endpoints import carts_url, carts_url, orders_url, products_url, register_url, status_url
from utils.secret import access_token

# TODO remove after debugging
from utils.secret import mock_cart_id, mock_item_id


# api actions
def get_status() -> Response:
    """ Returns response object with API status """
    return requests.get(status_url)


def get_all_products() -> Response:
    """ Returns response object with list of products in JSON format """
    return requests.get(products_url)


def get_product_by_id(product_id: int, label: bool=None) -> Response:
    """ Returns response object with product details in JSON format """
    payload = {"product-label": label}
    url = f"{products_url}/{product_id}"
    return requests.get(url, params=payload)


def create_cart() -> Response:
    """ Returns response object with cart details in JSON format """
    return requests.post(carts_url)


def get_cart_info(cart_id: str) -> Response:
    """ Returns response object with cart details in JSON format """
    url = f"{carts_url}/{cart_id}"
    return requests.get(url) 


def get_cart_items(cart_id: str) -> Response:
    """ Returns response object with list of items added to cart in JSON format """
    url = f"{carts_url}/{cart_id}/items"
    return requests.get(url)


def add_item_to_cart(cart_id: str, product_id: int) -> Response:
    """ Returns response object with add confirmation in JSON format """
    url = f"{carts_url}/{cart_id}/items"
    payload = {
        "productId": f"{product_id}"
    }
    return requests.post(url, json=payload)


def modify_item_in_cart(cart_id: str, item_id: int, quantity: int) -> Response:
    """ Returns response object with no text """
    url = f"{carts_url}/{cart_id}/items/{item_id}"
    payload = {
        "quantity": f"{quantity}"
    }
    return requests.patch(url, json=payload)


def replace_item_in_cart(cart_id: str, item_id: int, product_id: int, quantity: int) -> Response:
    """ Returns response object with no text """
    url = f"{carts_url}/{cart_id}/items/{item_id}"
    payload = {
        "productId": f"{product_id}",
        "quantity": f"{quantity}"
    }
    return requests.put(url, json=payload)


def delete_item_in_cart(cart_id: str, item_id: int) -> Response:
    """ Returns response object with no text """
    url = f"{carts_url}/{cart_id}/items/{item_id}"
    return requests.delete(url)


# TODO remove after debugging
print(get_cart_info(mock_cart_id).text)
# response = delete_item_in_cart(mock_cart_id, 153502116)
# print(response.text)
# print(response.request.url)
# print(response.request.body)
# print(response.request.headers)
