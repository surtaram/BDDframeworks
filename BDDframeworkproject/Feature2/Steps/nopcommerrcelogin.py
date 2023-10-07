from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


# @when('Launch the browser')
# def step_impl(context):
#     context.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# @when('Open the application url')
# def step_impl(context):
#     context.driver.get("https://demo.nopcommerce.com/")


@when('Clicked on Login')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@class='ico-login']").click()


@when('Enter "{username}" and "{password}"')
def step_impl(context,username,password):
    context.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(username)
    context.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys(password)


@when('Clicked on Log in')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@class='button-1 login-button']").click()

@when('Verify user successfully login')
def step_impl(context):
    try:
        text=context.driver.find_element(By.XPATH,"//div[@class='topic-block-title']").text
    except:
        assert False,"Test failed"
    if text=="Welcome to our store":
        assert True,"Test passed"
    else:
        assert False,"Test failed"

@when('Verify user validation message')
def step_impl(context):
    try:
        message=context.driver.find_element(By.XPATH,"//div[@class='message-error validation-summary-errors']").text
        print(message)
    except:
        assert False,"Test failed"
    if message=="Login was unsuccessful. Please correct the errors and try again.\nNo customer account found":
        assert True,"Test Passed"
    else:
        assert False,"Test Failed"

@when('Verify user validation message under email text box')
def step_impl(context):
    try:
        email_validation=context.driver.find_element(By.XPATH,"//span[@id='Email-error']").text
    except:
        assert False,"Test failed"
    if email_validation=="Please enter your email":
        assert True,"Test Passed"
    else:
        assert False,"Test Failed"


@when('Closed browser')
def step_impl(context):
    context.driver.close()


