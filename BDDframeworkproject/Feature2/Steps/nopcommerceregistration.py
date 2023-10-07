from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@when('Open the application')
def step_impl(context):
    context.driver.get("https://demo.nopcommerce.com/")

@when("Clicked on register")
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
@when("Maxmize the windows")
def step_impl(context):
    context.driver.maximize_window()

@when('Select Male as gender')
def step_impl(context):
    context.driver.implicitly_wait(5) # seconds
    gender_radio=context.driver.find_element(By.XPATH,"//input[@value='M']")
    gender_radio.click()


@when('Enter user "{firstname}"')
def step_impl(context,firstname):
    time.sleep(3)
    user_firstname=context.driver.find_element(By.XPATH,"//input[@name='FirstName']")
    user_firstname.send_keys(firstname)


@when('Enter users "{lastname}"')
def step_impl(context,lastname):
    time.sleep(3)
    Lastname=context.driver.find_element(By.XPATH,"//input[@name='LastName']")
    Lastname.send_keys(lastname)


@when('User select Day "{Day}"')
def step_impl(context,Day):
    Day_dropdown=Select(context.driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']"))
    Day_dropdown.select_by_value(Day)



@when('User select month "{Month}"')
def step_impl(context,Month):
    Month_dropdown=Select(context.driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']"))
    Month_dropdown.select_by_value(Month)





@when('User select Year "{Year}"')
def step_impl(context,Year):
    Year_dropdown=Select(context.driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']"))
    Year_dropdown.select_by_value(Year)


@when('Enter user email "{Email}"')
def step_impl(context,Email):
    User_email=context.driver.find_element(By.XPATH,"//input[@id='Email']")
    User_email.send_keys(Email)


@when('Enter user company name "{company_name}"')
def step_impl(context,company_name):
    company=context.driver.find_element(By.XPATH,"//input[@id='Company']")
    company.send_keys(company_name)


@when('Enter user password "{password}"')
def step_impl(context,password):
    user_password=context.driver.find_element(By.XPATH,"//input[@id='Password']")
    user_password.send_keys(password)


@when('Enter user confirm password"{Confirm_password}"')
def step_impl(context,Confirm_password):
    user_confirm_password=context.driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']")
    user_confirm_password.send_keys(Confirm_password)
    time.sleep(5)


@when('Click on Register')
def step_impl(context):
    register_button=context.driver.find_element(By.XPATH,"//button[@id='register-button']")
    register_button.click()
    time.sleep(4)

@when("Verify registration is completed")
def step_impl(context):
    try:
        text=context.driver.find_element(By.XPATH,"//div[@class='result']").text
    except:
        assert False,"Test failed"
    if text=="Your registration completed":
        assert True,"Test passed"
    else:
        assert False,"Test failed"





@when(u'Enter the "username" and "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter the "username" and "password"')


@when(u'click on login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on login')


@then(u'User must login the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User must login the page')
