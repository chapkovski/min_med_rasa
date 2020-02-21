## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## condition better
* wellness_check
  - action_wellness_q
* affirm OR condition_better
  - utter_condition_improved

## condition worse
* wellness_check
  - action_wellness_q
* deny OR condition_worse
  - utter_condition_worsened

## condition same
* wellness_check
  - action_wellness_q
* condition_same
  - utter_condition_same
