import email
from urllib.error import URLError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# create browser 
url = "https://demoqa.com/text-box"
browser = webdriver.Edge("C:/Users/Matasyan/Desktop/selenium/drivers/msedgedriver.exe")
browser.get(url)
browser.maximize_window()
expectedAddress = browser.current_url
time.sleep(2)
# checking that correct page is open
if expectedAddress == url:
    print("The correct page is opened")
else:
    print("The wrong page is opened")

# finding fields and filling them
fullName = browser.find_element(By.ID, 'userName')
fullName.send_keys("Mila")

eMail = browser.find_element(By.ID, 'userEmail') 
eMail.send_keys("milagasparyan@gmail.com")

currentAddress = browser.find_element(By.ID, 'currentAddress') 
currentAddress.send_keys("something")

permanentAddress = browser.find_element(By.ID, 'permanentAddress') 
permanentAddress.send_keys("something else")
time.sleep(1)

#clicking on submit button

action = ActionChains(browser)
submitButton = browser.find_element(By.ID, "submit")

action.move_to_element(submitButton)
time.sleep(2)
submitButton.send_keys(Keys.ENTER)
#action.click(submitButton).perform()


textBox = browser.find_element(By.ID, 'output')
actualText = textBox.text

expectedText = "Name:Mila\nEmail:milagasparyan@gmail.com\nCurrent Address :something\nPermananet Address :something else"
try:
    assert expectedText in actualText
    print ("the text is correct")
except:
    print("the text is incorect")

time.sleep(2)
browser.quit()
