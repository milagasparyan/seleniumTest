from project.Lib import LIB
from selenium.webdriver.common.by import By

class Home:

    #---locators---
    mango               = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[18]/div[3]/button[1]")
    cartIcon            = (By.XPATH, "//body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/a[4]/img[1]")    
    proceedToCheckout   = (By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
    items               = (By.XPATH, "//strong[contains(text(),'1')]")

    
    def __init__(self, browser):
        self.browser = browser

   #click to Add mango to cart
    def clickMango(self, browser ):
       LIB.wait_for_element(self,browser,self.mango)
       self.browser.find_element(*self.mango).click()
    
    #click to Cart icon
    def clickCartIcon(self, browser):
        LIB.wait_for_element(self, browser, self.cartIcon)
        self.browser.find_element(*self.cartIcon).click()

    #click to proceed to checkout
    def clickProceedCheckout(self,browser):
        LIB.wait_for_element(self, browser, self.proceedToCheckout)
        self.browser.find_element(*self.browser).click()
    


    