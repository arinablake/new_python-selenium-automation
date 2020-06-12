# Created by arina at 6/12/20
Feature: Test Scenarios for checking shopping cart on Amazon

  Scenario: User can check a shopping cart on Amazon
    Given Open Amazon page
    When Click Shopping Cart button
    Then Verify Your Amazon Cart is empty text present