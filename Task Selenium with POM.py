from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
browser = webdriver.Edge("C:/Users/Matasyan/Desktop/selenium/drivers/msedgedriver.exe")
action = ActionChains(browser)
browser.get(url)
window_before = browser.window_handles[0]
browser.maximize_window()
expectedAddress = browser.current_url
time.sleep(2)
assert expectedAddress == url

browser.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/div[18]/div[3]/button[1]").click()

##quantity=browser.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/div[18]/div[2]/input[1]")

##Items=browser.find_element_by_xpath("//strong[contains(text(),'1')]")

##if quantity == Items 
##print "equal"
##else
##print "non equal"

browser.find_element_by_xpath("//body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/a[4]/img[1]").click()

browser.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

browser.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()