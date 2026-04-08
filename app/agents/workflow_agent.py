from app.agents.task_agent import TaskAgent
from app.agents.calendar_agent import CalendarAgent

class WorkflowAgent:
    def __init__(self):
        self.task = TaskAgent()
        self.calendar = CalendarAgent()

    def run(self, req):
        results = []

        steps = req.get("steps", [])

        for step in steps:
            if step["type"] == "task":
                results.append(self.task.run(step))
            elif step["type"] == "calendar":
                results.append(self.calendar.run(step))

        return {"workflow_results": results}