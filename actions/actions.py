from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionConfirmMultipleItems(Action):
    def name(self) -> Text:
        return "action_confirm_multiple_items"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        items = tracker.get_slot("items")

        if items:
            # Formulate a response confirming the items in the order
            response = "Got it! You want "
            for idx, item in enumerate(items):
                response += f"{item['quantity']} {item['name']}"
                if idx < len(items) - 2:
                    response += ", "
                elif idx == len(items) - 2:
                    response += " and "
                else:
                    response += "."
            dispatcher.utter_message(text=response)
        else:
            dispatcher.utter_message(text="No items found in the order.")

        return []
