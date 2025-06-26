from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendPackage(Action):
    def name(self) -> Text:
        return "action_recommend_package"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product = tracker.get_slot("product_type")
        if product == "เครื่องกรองน้ำ":
            msg = "แนะนำรุ่น CHP-264L ผ่อนเพียง 790 บาท/เดือน"
        elif product == "เครื่องฟอกอากาศ":
            msg = "รุ่น AP-1516D พร้อมส่วนลดพิเศษ"
        else:
            msg = "เรามีสินค้าให้เลือกหลากหลาย สนใจดูเพิ่มเติมไหมคะ?"

        dispatcher.utter_message(text=msg)
        return []
