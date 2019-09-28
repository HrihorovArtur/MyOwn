Feature: Google Search

  Scenario: Ask google for job
    Given Navigate to google
    When I fill "QA job" text in search field
      And I click on "Search" button
    Then I should see "Remote QA Jobs" article