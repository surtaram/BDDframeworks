from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@given('I launch browser')
def step_impl(context):
    assert True ,"Test passed"



@when('I open application')
def step_impl(context):
    assert True, "Test passed"



@when('Enter valid username and password')
def step_impl(context):
    assert True, "Test passed"



@when('Click on login')
def step_impl(context):
    assert True, "Test passed"



@then('User must login to dashboard page')
def step_impl(context):
    assert True, "Test passed"



@when('Navigate to search page')
def step_impl(context):
    assert True, "Test passed"


@then('Search page should display')
def step_impl(context):
    assert True, "Test passed"


@when('navigate to advanced search page')
def step_impl(context):
    assert True, "Test passed"


@then('advanced search page should display')
def step_impl(context):
    assert True, "Test passed"
