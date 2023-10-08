from selenium import webdriver
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
#this file only for practice purpose
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
elements=driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']//child::input[@type='checkbox']")
print(len(elements))
for i in elements:
    # time.sleep(3)
    print(">>>>>>>",i.text)
    i.click()
#drop down handle
time.sleep(3)
drop=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
# drop.select_by_value("India")
drop.select_by_visible_text("India")

