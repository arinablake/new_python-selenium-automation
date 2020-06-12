# Created by arina at 6/12/20
Feature: Verify that user can add a searched item to the cart

  Scenario: User can add a searched item to the cart
    Given Open Amazon page
    When Input iPhone 11 phone into search field
    And Click search button
    And Choose first item
    And Add an item to shopping cart
    And See pop up 1 - Close pop up 1
    And See pop up 2 - Close pop up 2
    And Click Shopping Cart button
    Then iPhone in Shopping Cart is shown