Feature: Nopcommerce login

  Background: Comman steps
    Given Launch the browser
    When Open the application
    And Maxmize the windows
    And Clicked on Login




  @Sanity
  Scenario: Nop commerce user valid login credentials
    And Enter "ram14@gmail.com" and "xyz1234"
    And Clicked on Log in
    And Verify user successfully login
    And Closed browser
  @Sanity
  Scenario: Nop commerce user invalid pass and valid username
    And Enter "ram1@gmail.com" and "xyz124"
    And Clicked on Log in
    And Verify user validation message
    And Closed browser
  @Sanity
  Scenario: Nop commerce user invalid pass and invalid username
    And Enter "ram1ddadas@gmail.com" and "xyz124"
    And Clicked on Log in
    And Verify user validation message
    And Closed browser
  @Sanity
  Scenario: Nop commerce user empty pass and empty username
    And Enter " " and " "
    And Clicked on Log in
    And Verify user validation message under email text box
    And Closed browser







