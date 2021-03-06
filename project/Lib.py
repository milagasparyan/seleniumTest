from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys


'''
Lib class has the following methods
1. open_browser
2. page_load
4. move_to_element
5. wait_for_element
6. wait_for_elements
7. get_data
9. close_browser
10. get_page_title
'''

class LIB:
    #create Chrome driver
    def open_browser(self):
        try:
            with open('config.json') as f:
                data = json.load(f)
            browser = webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print("Something went wrong during browser opening!")

    #navigate to given url-page
    def page_load(self, browser):
        try:
            with open('config.json') as f:
                data = json.load(f)
            browser.get(data['url'])
        except:
            print("Somthing wrong with page_load!")

    # move to givvent element
    def move_to_element(self, browser, element):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print("Can not move to given element!")              

    # wait for given element to be vissible in UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser,100).until(EC.visibility_of_element_located(element))

        except:
            print("Element is not visible!")    

     # wait for given element to be vissible in UI
    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser,100).until(EC.visibility_of_any_elements_located(elements))
        except:
            print("Elements are not visible!")   

    #data parsing
    def get_data(self, key):
        try:
            with open('data.json') as f:
                data = json.load(f)
            return data[key]
        except:
            print("Error during data getting!")     

    #close browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print ("Driver is not closed!")     
            
    def getTitle(self, browser):
        try:
            getTitle = browser.title
        except:
            print ("Can't get title")               