import sys
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/utils')
from file_operations import write_to_json, read_from_json
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from task import Task


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.name = email.split('@')[0]
        self._save_user_to_database()

    def set_name(self, name):
        self.name = name
        self._save_user_to_database()

    def assign_task(self, Task):
        Task['assignee'] = self.name

    def _save_user_to_database(self):
        data = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        write_to_json(data, f'../data/users/{self.email.split("@")[0]}.json')
