# Created by arina at 6/17/20
Feature: Verify that user can see specified amount of links on amazon bestsellers page

  Scenario: User can see specified amount of links on amazon bestsellers page
    Given Open Amazon page
    When Click bestsellers link
    Then Verify that there are 5 links on amazon bestsellers page