from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
@given("I launch chrome browser")
def step_impl(context):
    # added headless mode in script
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


@when('I open orange hrm home page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter user name {user} and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

@then('User must successfully login to the dashboard page')
def step_impl(context):
    try:
        text=context.driver.find_element(By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']").text
    except:
        assert False ,'Test Failed'
    if text=='Dashboard':
        context.driver.close()
        assert True,"Test Passed"
    else:
        assert False ,"Test Failed"








