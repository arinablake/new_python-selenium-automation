# Created by arina at 6/12/20
Feature: Test Scenarios for search for Cancelling an order on Amazon

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon help page
    When Input Cancel order into help search field
    And Click go button
    Then Cancel order page is shown
