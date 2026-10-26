from enum import Enum
from fastapi import FastAPI

app = FastAPI(title="Production-Style Task API")


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


users = [
    {"id": 1, "name": "Rahul", "city": "Jaipur", "status": TaskStatus.pending, "priority": TaskPriority.low},
    {"id": 2, "name": "Aman", "city": "Delhi", "status": TaskStatus.pending, "priority": TaskPriority.low},
    {"id": 3, "name": "Priya", "city": "Jaipur", "status": TaskStatus.pending, "priority": TaskPriority.low},
]


@app.get("/tasks")
def get_tasks(status: TaskStatus = TaskStatus.pending, priority: TaskPriority = TaskPriority.low, limit: int = 10):
    filtered_tasks = [t for t in users if t['status'] == status and t['priority'] == priority][:limit]
    return filtered_tasks