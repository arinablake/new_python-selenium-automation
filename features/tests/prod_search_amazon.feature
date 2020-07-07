# Created by arina at 7/6/20
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Watches
    Then Product results for Watches are shown
