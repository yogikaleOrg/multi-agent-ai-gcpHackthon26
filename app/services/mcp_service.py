events = []

def schedule_event(req):
    event = {
        "id": len(events) + 1,
        "title": req.get("title"),
        "time": req.get("time")
    }
    events.append(event)
    return event

def list_events():
    return events

def get_event(id):
    for event in events:
        if event["id"] == id:
            return event