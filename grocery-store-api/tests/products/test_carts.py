import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import pytest
import utils.api_actions as api
from utils.parametrize import get_testdata


# TODO write tests
""" create cart, check cart info """

""" create cart, add 1 product in stock, check cart content """
""" create cart, add 1 product NOT in stock, check error message & cart content """

""" create cart, add 1 product, valid quantity, check cart content """
""" create cart, add 1 product invalid quantity (bigger than stock), check error & cart content """

""" cart with n products, change quantity """


# need more info
""" add product, add maximum products, check cart content - max not defined"""
""" add product, add maximum + 1 products, check error - max not defined"""
