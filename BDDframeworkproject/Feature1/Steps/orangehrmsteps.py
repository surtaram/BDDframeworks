from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



@given('launch chrome browser')
def launchBrowser(context):
    # added headless mode in script
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


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


