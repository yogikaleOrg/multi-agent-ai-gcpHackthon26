from app.services.google_calendar import schedule_event
from app.services.llm_service import extract_entities

class CalendarAgent:
    def run(self, req):
        text = req.get("input")

        data = extract_entities(text)

        title = data.get("title", "Meeting")
        time = data.get("time")

        if not time:
            return {"error": "Time not found in input"}

        event = schedule_event(title, time)

        return {
            "message": "Event scheduled successfully",
            "title": title,
            "time": time,
            "event": event
        }