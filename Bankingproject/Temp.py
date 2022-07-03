"""1. Open the page https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
2. Click on the "Bank Manager Login"
3. Add Customer
4. Accept the alert  popup
5. Click on the "Customers"
6. Search the customer on Customers list 
7. Assert that customer is added with correct info
8. Delete customer
9. Assert that customer is deleted"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


url = " https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
browser = webdriver.Edge("C:/Users/Matasyan/Desktop/selenium/drivers/msedgedriver.exe")
browser.get(url)
browser.maximize_window()
firstName = "Mila"
lastName = "Gasparyan"
postCode = 1111
#bankManagerLoginButton = (By.XPATH, "//button[@ng-click = 'manager()')]")
#addCustomerButton      = (By.XPATH, "//button[@ng-class='btnClass1']")
#firstNameField         =  (By.XPATH, "//div[@class= 'form-group']//input[@ng-model='fName']")
#lastNameFIeld          =  (By.XPATH, "//div[@class= 'form-group']//input[@ng-model='lName']")
#postCodeFiled          = (By.XPATH, "//div[@class= 'form-group']//input[@ng-model='lName']")
#customersButton        = (By.XPATH, "//button[@ng-class='btnClass3']")
#searchCustomerField    = (By.XPATH, "//input[@ng-model='searchCustomer']")
#deleteButton           = (By.XPATH, "//button[contains(text(),'Delete')]")
time.sleep(1) 
browser.find_element_by_xpath("//button[@ng-click = 'manager()']").click()
time.sleep(1) 
browser.find_element_by_xpath("//button[@ng-class='btnClass1']").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@class= 'form-group']//input[@ng-model='fName']").send_keys(firstName)
time.sleep(1)
browser.find_element_by_xpath("//div[@class= 'form-group']//input[@ng-model='lName']").send_keys(lastName)
time.sleep(1)
browser.find_element_by_xpath("//div[@class= 'form-group']//input[@ng-model='postCd']").send_keys(postCode)
browser.find_element_by_xpath("//button[@class='btn btn-default']").click()
time.sleep(1)
alert = browser.switch_to_alert()
alert.accept()
time.sleep(1)
browser.find_element_by_xpath("//button[@ng-class='btnClass3']").click()
time.sleep(1)
browser.find_element_by_xpath("//input[@ng-model='searchCustomer']").send_keys(firstName)
time.sleep(1)
browser.find_element_by_xpath("//button[contains(text(),'Delete')]").click()




