Feature: Nop commerce Registration

  Background: Common step
    Given Launch the browser
    When Open the application
    And Clicked on register
    And Maxmize the windows

  @Sanity
  Scenario: User registration
    And Select Male as gender
    And Enter user "ram"
    And Enter users "kumar"
    And User select Day "2"
    And User select Month "4"
    And User select Year "1998"
    And Enter user email "ram14@gmail.com"
    And Enter user company name "xyz"
    And Enter user password "xyz1234"
    And Enter user confirm password"xyz1234"
    And Click on Register
    And Verify registration is completed






