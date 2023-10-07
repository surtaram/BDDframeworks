from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




@given('launch chrome browser')
def launchBrowser(context):
    context.driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('open orangeHRM homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo present on page')
def verifylogo(context):
    status=context.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()


