import sys
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/utils')
from file_operations import write_to_json, read_from_json
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
import datetime as dt
from task import Task
import re


class Space:
    def __init__(self,
                 space_name: str,
                 created_at: dt,
                 tasks_json: list[dict],
                 already_in_db: bool):
        self.name = space_name
        self.created_at: dt = dt.datetime.strptime(created_at, "%d/%m/%Y %H:%M:%S")
        self.priority: int = 0
        self.tasks: list[Task] = self._create_tasks(tasks_json)
        self.already_in_db: bool = already_in_db

    @staticmethod
    def _create_tasks(tasks_json: list[dict]) -> list[Task]:
        tasks = []
        for task_data in tasks_json:
            task = Task(task_data)
            tasks.append(task)
        return tasks

    def __str__(self):
        return f"""Space {self.name} ({len(self.tasks)} tasks)"""

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
        space_dict = {
            "name": self.name,
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            "tasks": self._convert_tasks_to_json(self.tasks)
        }
        write_to_json(space_dict, f'../data/spaces/{self.name}.json')

    def add_task(self, task_dict):
        new_task = Task(task_dict)
        self.tasks.append(new_task)
        self.save_to_database()

    def add_task_from_input(self):
        new_task = {}
        description = input("Give task description: ")
        assignee = input("Who will be assignee: ")
        due_date = input("Give due date (format 24/12/2022): ")
        priority = int(input("Set priority (1-3):"))
        time_logged = input("Provide time logged (format 09:25:59): ")
        is_complete = self._make_bool(input("Is the task complete (yes/no): "))
        tags = self._separate_tags(input("Provide tags for it: (Finish the with . or !):"))
        comments = self._comment_maker()


    @staticmethod
    def _make_bool(argument):
        if argument == "yes":
            return True
        else:
            return False

    @staticmethod
    def _separate_tags(tags):
        tags = [tag for tag in re.split(r'[.!]', tags) if tag]
        return tags

    @staticmethod
    def _comment_maker():
        have_a_comment = True
        comments = []
        while have_a_comment:
            validation = input("Do you have a comment (yes/no): ")
            if validation == 'yes':
                author = input("Who's the author: ")
                text = input("What's the text of the comment: ")
                comments.append({'author': author, 'text': text})
            if validation == 'no':
                have_a_comment = False
        return comments
