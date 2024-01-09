import datetime, sys
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/utils')
from file_operations import write_to_json, read_from_json
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from task import Task
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from space import Space
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/scripts')


def main():

    # write_to_json(test_dict, '../data/spaces/test-spaces.json')
    # data = read_from_json('../data/spaces/test-spaces.json')
    # print(data)

    # new_task_dict = {
    #     'description': "Learn Python",
    #     'assignee': 'Kuba',
    #     "due_date": '08/01/2024',
    #     'priority': 2,
    #     'time_logged': "0:0:32",
    #     'is_complete': False,
    #     'tags': [],
    #     'comments': []
    # }
    # task = Task(new_task_dict)
    # print(task.description)
    # task.edit_description("Write Task-Manager Project")
    # print(task.description)
    #
    # print(task.is_complete)
    # task.mark_as_complete()
    # print(task.is_complete)
    # task.mark_as_complete()
    #
    # task.change_priority(5)
    # print(task.priority)
    # task.change_priority(3)
    # print(task.priority)
    #
    # task.log_time(datetime.timedelta(minutes=32))
    # print(task.time_logged)
    #
    # comment = {
    #     "author": "Jane",
    #     "text": "Better later than never."
    # }
    # task.add_comment(comment)
    # print(task.comments)
    #
    # print(task)

    task_list_of_dicts = [{
        'description': "Learn Python",
        'assignee': 'Kuba',
        "due_date": '08/01/2024',
        'priority': 2,
        'time_logged': "0:0:32",
        'is_complete': False,
        'tags': [],
        'comments': []
    }]

    new_task_dict = {
            'description': "Zad 2",
            'assignee': 'Jadzia',
            "due_date": '08/01/2024',
            'priority': 2,
            'time_logged': "0:0:32",
            'is_complete': False,
            'tags': [],
            'comments': []
        }

    space = Space("programowanie", "08/01/2024 00:00:00", task_list_of_dicts, False)
    space.add_task(new_task_dict)
    print(space.tasks[0])
    print(space.tasks[1])


if __name__ == '__main__':
    main()
