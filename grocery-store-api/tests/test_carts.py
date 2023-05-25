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
    cart_json = create_response.json()
    assert cart_json["created"] == True, "Created should be True"
    assert type(cart_json["cartId"]) == str, "Cart ID should be a string"
    assert len(cart_json["cartId"]) > 0, "Card ID length should be bigger than 0"
    cart_id = cart_json["cartId"]

    get_response = api.get_cart_info(cart_id)
    assert get_response.status_code == 200, "Status code should be 200"
    assert "items" in get_response.json().keys(), "items key should be in the json response"
    
    
@pytest.mark.parametrize("product_id", get_testdata("product_list.json", "test_cart_add_one_product"))
def test_cart_add_one_product(product_id):
    """ create cart, add 1 product in stock, check if added and cart items """
    create_response = api.create_cart()
    assert create_response.status_code == 201, "Status code should be 201"
    cart_id = create_response.json()["cartId"]

    add_response = api.add_item_to_cart(cart_id, product_id)
    assert add_response.status_code == 201, "Status code should be 201"
    assert add_response.json()["created"] == True
    
    cart_info_response = api.get_cart_items(cart_id)
    assert cart_info_response.status_code == 200, "Status code should be 200"
    for item in cart_info_response.json():
        assert item["productId"] == int(product_id)
        assert item["quantity"] == 1
    

# TODO write tests
""" create cart, add 1 product NOT in stock, check error message & cart content """

""" create cart, add 1 product, valid quantity, check cart content """
""" create cart, add 1 product invalid quantity (bigger than stock), check error & cart content """

""" cart with n products, change quantity """


# need more info
""" add product, add maximum products, check cart content - max not defined"""
""" add product, add maximum + 1 products, check error - max not defined"""
