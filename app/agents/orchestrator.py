from app.services.llm_service import classify_intent
from app.agents.task_agent import TaskAgent
from app.agents.calendar_agent import CalendarAgent
from app.agents.notes_agent import NotesAgent

class Orchestrator:
    def __init__(self):
        self.task = TaskAgent()
        self.calendar = CalendarAgent()
        self.notes = NotesAgent()

    def handle(self, req):
        text = req.get("input")

        if not text:
            return {"error": "Input prompt required"}

        intent = classify_intent(text)

        if intent == "task":
            return self.task.run(req)

        elif intent == "calendar":
            return self.calendar.run(req)

        elif intent == "notes":
            return self.notes.run(req)

        return {
            "message": "Could not determine intent",
            "intent": intent
        }