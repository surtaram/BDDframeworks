Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open orange hrm home page
    And Enter user name "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page

  Scenario Outline: : Login to OrangeHRM with multiple parameters
    Given I launch chrome browser
    When I open orange hrm home page
    And Enter user name "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the dashboard page

    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin124 |
      | admin    | adminxyz |
