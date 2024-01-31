import datetime as dt, os, sys

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from space import Space
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/utils')
from file_operations import write_to_json, read_from_json
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')


class TaskManager:
    def __init__(self, app_name):
        self.name: str = app_name
        self.spaces: dict[str, Space] = self._load_spaces()

    def __repr__(self):
        return f"TaskManager (name={self.name}"

    def __str__(self):
        return self.name

    @staticmethod
    def _load_spaces():
        directory_path = '/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/data/spaces'
        files_list = os.listdir(directory_path)
        files_list = [file.split('.')[0] for file in files_list if file.split('.')[0] != '__init__']
        files_paths = [directory_path + '/' + file + '.json' for file in files_list]
        spaces = {}
        for file, path in zip(files_list, files_paths):
            space_data = read_from_json(path)
            given_space = Space(space_data['name'], space_data['created_at'], space_data['tasks'], True)
            spaces[file] = given_space
        return spaces

    def add_space(self, space_name):
        if self._validate_space(space_name):
            created_at = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tasks = []
            new_space = Space(space_name, created_at, tasks, self._validate_space(space_name))
            self.spaces[space_name] = new_space
            return new_space
        else:
            print(f"Space \"{space_name}\" already exists. Please choose another name.")


    def _validate_space(self, space_name):
        if space_name in self.spaces:
            return False
        else:
            return True
