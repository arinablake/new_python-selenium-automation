# Created by arina at 6/26/20
Feature: Verify that every product on the page has a text ‘Regular’ and a product name
  # Enter feature description here

  Scenario: User can verify that every product on the page has a text ‘Regular’ and a product name
    Given Open Amazon Whole Foods deals page
    Then Verify, every product on the page has a text Regular
    Then Verify, every product on the page has a product name
