from project.Lib import LIB
from project.POM import Home
from selenium import webdriver

"""
Go to URL, click on mango add to card and ,
click on the cart icon, click proceed to checkout
"""

def test_1():
    #open browser
    obj_lib = LIB()
    browser = obj_lib.open_browser()

    #navigate to url
    obj_lib.page_load(browser)

    #assert page title
    actualTitle = obj_lib.getTitle(browser)
    expectedTitle = "GreenKart - veg and fruits kart"
    assertEqual(actualTitle,expectedTitle)




