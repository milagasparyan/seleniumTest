from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


url = "https://www.rahulshettyacademy.com/AutomationPractice/"
browser = webdriver.Edge("C:/Users/Matasyan/Desktop/selenium/drivers/msedgedriver.exe")
action = ActionChains(browser)
browser.get(url)
window_before = browser.window_handles[0]
browser.maximize_window()
expectedAddress = browser.current_url
time.sleep(2)
assert expectedAddress == url


# Select the radio button

browser.find_element_by_xpath("//input[@value='radio2']").click()

#Select an item from the static dropdown

browser.find_element_by_id('dropdown-class-example').click()
browser.find_element_by_xpath("//option[contains(text(),'Option1')]").click()

# Select checkbox

browser.find_element_by_xpath("//input[@value='option2']").click()

# Select an item from the dynamic dropdown

ClassExample = browser.find_element(By.ID, 'autocomplete')
ClassExample.send_keys("Armenia")
time.sleep(2)
browser.find_element(By.ID,'ui-id-1').click()

# Work with multiple windows and tabs

browser.find_element_by_id('openwindow').click()
window_after = browser.window_handles[1]
browser.switch_to.window(window_after)
time.sleep(2)
browser.switch_to.window(window_before)
browser.find_element_by_id('opentab').click()
time.sleep(2)
browser.switch_to.window(window_before)

# Handle Alerts
AlertExample = browser.find_element(By.ID, 'name')
AlertExample.send_keys("Mila")
browser.find_element_by_id('alertbtn').click()
Alert(browser).accept()
time.sleep(2)

# Work with the hide and show elements section and use assertions
# Scroll the table

browser.execute_script("window.scrollTo(0, 1080)")
browser.find_element_by_id('hide-textbox').click()
time.sleep(2)
browser.find_element_by_id('show-textbox').click()
time.sleep(2)

# Mouse hover on the element

MouseHover = browser.find_element(By.ID, 'mousehover')
action.move_to_element(MouseHover)
action.perform()
time.sleep(2)
browser.find_element_by_xpath("//a[contains(text(),'Top')]").click()

#Work with iframes

iFrame = browser.find_element(By.ID, "courses-iframe")
browser.switch_to.frame(iFrame)
browser.find_element_by_link_text('Courses').click()

browser.quit()