Feature: Test
    Scenario: Test Builder
      Given Service_Builder
      When test_AnnaLafargue_builder return OK
      And test_Luminarc_builder return OK
      Then Good job
