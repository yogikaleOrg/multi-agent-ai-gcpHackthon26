from app.db.database import save_note
from app.services.llm_service import extract_entities

class NotesAgent:
    def run(self, req):
        text = req.get("input")

        data = extract_entities(text)

        content = data.get("content")

        if not content:
            return {"error": "Note content missing"}

        save_note(content)

        return {
            "message": "Note saved",
            "content": content
        }