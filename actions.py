from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from reasons import reasons


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_wellness_q"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("TRACKER", tracker.latest_message)
        reason = next(tracker.get_latest_entity_values("reason"), None)
        print("REASON!!!", reason)
        reason_desc = reasons.get(reason)
        print("REASON DESC", reason_desc)
        if reason:
            if reason_desc:
                resp = f' Hey, we just wanted to touch base with you because {reason_desc}'
            else:
                # some fallback if reason description is not found in DB
                resp = f' Hey, we just wanted to touch base with you because ... dont know why'
        else:
            resp = "Hey, we just wanted to touch base, and see how you were doing. Are you feeling any better?"
        dispatcher.utter_message(text=resp)
        return []
