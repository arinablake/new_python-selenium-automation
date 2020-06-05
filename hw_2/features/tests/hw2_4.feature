# Created by arina at 6/5/20
Feature: Test Scenarios for logged out user sees Sign in page when clicking Orders


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open https://www.amazon.com
    When Click Orders
    Then Verify Sign in page opened
