Feature: OrangeHRM Logo
  Scenario: Logo present on orangHRM homepage
    Given launch chrome browser
    When open orangeHRM homepage
    Then verify that the logo present on page
    And close browser
