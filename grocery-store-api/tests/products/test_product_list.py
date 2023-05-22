import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import utils.api_actions as api

def test_products_list_is_returned():
    """ Check if the list of products is returned and contains products """
    response = api.get_all_products()
    assert response.status_code == 200, "Status code should be 200"
    assert len(response.json()) > 0, "Product list is too short"
    assert isinstance(response.json()[0], dict), "Item in product list is not JSON object"


def test_products_list_has_20_items():
    """ Product list should have 20 items by default """
    response = api.get_all_products()
    assert response.status_code == 200, "Status code should be 200"
    assert not len(response.json()) > 20, "Product list has more than 20 products"
    assert not len(response.json()) < 20, "Product list has less than 20 products"


def test_product_list_only_requested_category():
    # TODO: remove hardcoded value; repeat test case for all available categories
    """ Product list should have only items from selected category """
    category = "dairy"
    response = api.get_all_products(category=category)
    assert response.status_code == 200, "Status code should be 200"
    for item in response.json():
        assert item["category"] == category, "Product has incorrect category"


def test_product_list_max_result_number():
    # TODO: remove hardcoded value; repeat test case for all numbers 0 - 20
    """ Product list should have only the requested number of items """
    requested_results = 1
    response = api.get_all_products(max_results=requested_results)
    assert response.status_code == 200, "Status code should be 200"
    assert len(response.json()) <= requested_results, "List length does not match the number of results"


def test_product_list_only_in_stock():
    """ Product list should only include items in stock """
    response = api.get_all_products(is_available="true")
    assert response.status_code == 200, "Status code should be 200"
    for item in response.json():
        assert item["inStock"] == True, "Product is not in stock"


def test_product_list_only_sold_out():
    """ Product list should only include items that are sold out """
    response = api.get_all_products(is_available="false")
    assert response.status_code == 200, "Status code should be 200"
    for item in response.json():
        assert item["inStock"] == False, "Product is not sold out"