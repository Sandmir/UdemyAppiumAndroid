Feature: Test login features

  Scenario: User can login with valid credentials
    Given Login with: username "marina_sen@list.ru" and psw "Portnov12345"
    Then Go to main menu
    Then Verify username: "Marina Senyutina"

  Scenario: User can't login with valid login and invalid password
    Given Login with: username "marina_sen@list.ru" and psw "Portnov123456"
    Then Verify error message "Please check your email and password." is displayed


  Scenario: User can't login with invalid login and valid password
    Given Login with: username "marina_sen1@list.ru" and psw "Portnov12345"
    Then Verify error message "Please check your email and password." is displayed

  @wip
  Scenario: User can logout
    Given Login with: username "marina_sen@list.ru" and psw "Portnov12345"
    Then Go to main menu
    And Logout
    Then Verify button "Sign in" is displayed


