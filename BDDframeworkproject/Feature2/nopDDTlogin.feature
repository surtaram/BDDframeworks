Feature: Login using DDT

  Scenario Outline:Login to nopcommerce with multiple data
    Given Launch the browser
    When Open the application
    And Maxmize the windows
    And Clicked on Login
    And Enter "<email>" and "<password>"
    And Clicked on Log in
    And Verify user successfully login

    Examples:
      | email              | password |
      | ram14@gmail.com    | admin123 |
      | admin123@gmail.com | xyz1234  |
      | ram14@gmail.com    | xyz1234  |
      | admin@gmail.com    | adminxyz |

