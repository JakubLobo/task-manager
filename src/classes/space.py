import datetime as dt
from task import Task


class Space:
    def __init__(self,
                 space_name: str,
                 created_at: dt,
                 tasks_json: list[dict],
                 already_in_db: bool):
        self.name = space_name
        self.created_at: dt = created_at
        self.priority: int = 0
        self.tasks = tasks_json
        self.already_in_db = already_in_db

    @staticmethod
    def _create_tasks(tasks_json: list[dict]) -> list[Task]:
        tasks = []
        for task_data in tasks_json:
            task = Task(task_data)
            tasks.append(task)
        return tasks

    def __str__(self):
        return f"""Space {self.name} ({len(self.tasks)}"""

    def __repr__(self):
        return f"""Space(name={self.name}, n_tasks={len(self.tasks)}"""

    @staticmethod
    def _convert_tasks_to_json(tasks):
        task_list = [{'description': task.description,
                      'assignee': task.assignee,
                      'due_date': task.due_date.strftime("%d/%m/%Y"),
                      'priority': task.priority,
                      'time_logged': str(task.time_logged),
                      'is_complete': task.is_complete,
                      'tags': task.tags,
                      'comments': task.comments
                      } for task in tasks]
        return task_list

    def save_to_database(self):

