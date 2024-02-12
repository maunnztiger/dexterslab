# Testcase Reporting tool basic functions
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

print("Testing started: Definition of Start")
driver = webdriver.Firefox()
driver.get("http://localhost:8080")
driver.maximize_window()
title = driver.title
assert "Homeoffice" in title
print("Test 0: `title` test passed")
sleep(1)
menu_button = driver.find_element(by=By.ID,value="menuButton")
menu_button.click()
driver.find_element(by=By.LINK_TEXT, value="Homeoffice general data")
driver.find_element(by=By.LINK_TEXT, value="Men in Homeoffice data")
driver.find_element(by=By.LINK_TEXT, value="Homeoffice Special data")
print("Test 1: `menu-links` test passed")
sleep(1)
menu_link_general = driver.find_element(by=By.LINK_TEXT, value="Homeoffice general data")
menu_link_general.click()
table_id = driver.find_element(By.XPATH, "//table[@id='table_raw']")
print("Test 2: `table-load succesfully` test passed")
return_button = driver.find_element(by=By.ID,value="returnButton")
return_button.click()
print("Test 3: `return button` test passed")
driver.find_element(by=By.ID,value="menuButton")
driver.quit()

print("SUCCESS: Definition of Done completed")


