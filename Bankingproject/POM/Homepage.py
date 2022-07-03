from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class Homepage:



    #locators
    bankManagerLoginButton = (By.XPATH, "//button[@ng-click = 'manager()')]")
    url = " https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    #browser
    browser = webdriver.Edge(".\Bankingproject\drivers\msedgedriver.exe")



    #methods
    def openHomePage(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def clickManagerLogin (self):
        WebDriverWait(self.browser,100).until(EC.visibility_of_element_located(self.bankManagerLoginButton))
        self.browser.find_element(self.bankManagerLoginButton).click()




