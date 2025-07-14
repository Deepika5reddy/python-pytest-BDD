Feature: e2e API validation
@smoke
  Scenario: Validate User
    Given Base url
    When Perform get call
    Then assert 200
@smoke
   Scenario Outline: Register a new user
    Given I set the base URL for POST request
    And I prepare the signup user payload
    When I perform a POST call to register user
    Then the response status should be 200
    And the response should contain user <id> and token "QpwL5tke4Pnpja7X4"

     Examples:
     | id |
     | 4  |


  @regression
  Scenario: Delete an existing user
    Given I set the base URL for DELETE request
    When I perform the DELETE call
    Then the response status should be "204"
