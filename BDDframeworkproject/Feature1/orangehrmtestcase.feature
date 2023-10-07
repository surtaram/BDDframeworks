Feature: OrangeHRM login

  Background: common step
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on login


  Scenario: Login to hrm application
    Then User must login to dashboard page

  Scenario: Search user
    When Navigate to search page
    Then Search page should display

  Scenario:Advanced search user
    When navigate to advanced search page
    Then advanced search page should display

