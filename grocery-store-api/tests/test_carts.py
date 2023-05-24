import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import pytest
import utils.api_actions as api
from utils.parametrize import get_testdata

def test_cart_info():
    """ create cart, check cart is created and info can be retrieved """
    create_response = api.create_cart()
    assert create_response.status_code == 201, "Status code should be 201"
    create_data = create_response.json()
    assert create_data["created"] == True, "Created should be True"
    assert type(create_data["cartId"]) == str, "Cart ID should be a string"
    assert len(create_data["cartId"]) > 0, "Card ID length should be bigger than 0"
    cart_id = create_data["cartId"]
    get_response = api.get_cart_info(cart_id)
    assert get_response.status_code == 200, "Status code should be 200"
    assert "items" in get_response.json().keys(), "items key should be in the json response"
    

# TODO write tests
""" create cart, add 1 product in stock, check cart content """
""" create cart, add 1 product NOT in stock, check error message & cart content """

""" create cart, add 1 product, valid quantity, check cart content """
""" create cart, add 1 product invalid quantity (bigger than stock), check error & cart content """

""" cart with n products, change quantity """


# need more info
""" add product, add maximum products, check cart content - max not defined"""
""" add product, add maximum + 1 products, check error - max not defined"""
