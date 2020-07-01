# Created by arina at 6/30/20
Feature: Verify that user can see matching description after clicking relevant tab
  # Enter feature description here

  Scenario: User can see matching description after clicking relevant tab
    Given Open Amazon page
    When Click bestsellers link
    Then Verify that each tab has a matching banner