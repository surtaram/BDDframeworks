from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time



@given('Launch the browser')
def step_impl(context):
    # added headless mode in script
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


@when('Open the application')
def step_impl(context):
    context.driver.get("https://testautomationpractice.blogspot.com/")

@when('Enter user name "{name}"')
def step_impl(context,name):
    context.driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)



@when('Enter user email "{email}"')
def step_impl(context,email):
    context.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(email)



@when('Enter user phone "{phone}"')
def step_impl(context,phone):
    context.driver.find_element(By.XPATH,"//input[@id='phone']").send_keys(phone)


@when('Enter user address "{address}"')
def step_impl(context,address):
    context.driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys(address)


@when('Select radio button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@id='male']").click()

@when('Select checkboxes')
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']//child::input[@type='checkbox']")
    for i in elements:
        i.click()
@when('Select country')
def step_impl(context):
    country=Select(context.driver.find_element(By.XPATH,"//select[@id='country']"))
    country.select_by_visible_text("India")

@when('Select colours')
def step_impl(context):
    colours=Select(context.driver.find_element(By.XPATH,"//select[@id='colors']"))
    colours.select_by_visible_text("Red")


@when('Select date')
def step_impl(context):
    pass

@when('Print all the value from web table')
def step_impl(context):
    pass








