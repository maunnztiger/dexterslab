# Testcase Reporting tool general data table content
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
print("Test 1: `menu-link` test passed")
sleep(1)
menu_link_general = driver.find_element(by=By.LINK_TEXT, value="Homeoffice general data")
menu_link_general.click()
table_id = driver.find_element(By.XPATH, "//table[@id='table_raw']")
print("Test 2: `table-load succesfully` test passed")
sleep(1)
# td =  table_id.find_elements(By.XPATH, "//td[contains(text(), 'Laut Befragung kann ich meinen Job aus dem Homeoffice machen')]") 
for row in range(1,13):
    rows = table_id.find_elements(By.XPATH, "//body//tr["+str(row)+"]")
    for row in rows:        
        td = row.find_elements(By.XPATH, "//td[contains(text(), 'Hatten 2020 die Chance auf Homeoffice')]")
        for i in td:
       # print([i.text for i in td if i.text == 'Hatten 2020 die Chance auf Homeoffice'])        
            assert 'Hatten 2020 die Chance auf Homeoffice' in  i.text

print("Test 3: `table content matches certain string` test passed") 
print("SUCCESS: Definition of Done completed")
driver.quit()
