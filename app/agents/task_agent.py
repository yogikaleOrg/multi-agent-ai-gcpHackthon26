from app.db.database import save_task
from app.services.llm_service import extract_entities

class TaskAgent:
    def run(self, req):
        text = req.get("input")

        data = extract_entities(text)

        title = data.get("title")
        priority = data.get("priority", "medium")

        if not title:
            return {"error": "Task title missing"}

        save_task(title, priority)

        return {
            "message": "Task created",
            "title": title,
            "priority": priority
        }