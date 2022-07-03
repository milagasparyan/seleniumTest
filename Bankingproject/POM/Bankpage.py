from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

class Bankpage:


        #locators

        addCustomerButton      = (By.XPATH, "//button[@ng-class='btnClass1']")
        firstNameField         =  (By.XPATH, "//div[@class= 'form-group']//input[@ng-model='fName']")
        lastNameField          =  (By.XPATH, "//div[@class= 'form-group']//input[@ng-model='lName']")
        postCodeField          = (By.XPATH, "//div[@class= 'form-group']//input[@ng-model='lName']")
        customersButton        = (By.XPATH, "//button[@ng-class='btnClass3']")
        searchCustomerField    = (By.XPATH, "//input[@ng-model='searchCustomer']")
        deleteButton           = (By.XPATH, "//button[contains(text(),'Delete')]")

        #browser
        browser = webdriver.Edge(".\Bankingproject\drivers\msedgedriver.exe")


        def clickaddCustomerButton (self):
            WebDriverWait(self.browser,100).until(EC.visibility_of_element_located(self.addCustomerButton))
            self.browser.find_element(self.addCustomerButton).click()

        def fillFields(self, firstName,lastName, postCode):
            WebDriverWait(self.browser,100).until(EC.visibility_of_element_located(self.postCodeField))
            self.browser.find_element(self.firstNameField).send_keys(firstName)
            self.browser.find_element(self.firstNameField).send_keys(lastName)
            self.browser.find_element(self.firstNameField).send_keys(postCode)

        def clickcustomersButton (self):
            WebDriverWait(self.browser,100).until(EC.visibility_of_element_located(self.customersButton))
            self.browser.find_element(self.customersButton).click()
        
        def searchCustomer (self, firstName,lastName, postCode ):
            WebDriverWait(self.browser,100).until(EC.visibility_of_element_located(self.searchCustomerField))
            self.browser.find_element(self.searchCustomerField).send_keys(firstName + lastName + postCode)

        def clickDeleteButton (self):
            WebDriverWait(self.browser,100).until(EC.visibility_of_element_located(self.searchCustomerField))
            self.browser.find_element(self.deleteButton).click() 









