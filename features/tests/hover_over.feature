# Created by arina at 7/25/20
Feature: Verify that user can see the deals when hovers over New Arrivals
  # Enter feature description here

  Scenario: User can see the deals when hovers over New Arrivals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then User can see the deals
