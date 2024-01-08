import datetime, sys
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/utils')
from file_operations import write_to_json, read_from_json
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from task import Task
sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/scripts')


def main():

    # write_to_json(test_dict, '../data/spaces/test-spaces.json')
    # data = read_from_json('../data/spaces/test-spaces.json')
    # print(data)

    new_task_dict = {
        'description': "Learn Python",
        'assignee': 'Kuba',
        "due_date": '08/01/2024',
        'priority': 2,
        'time_logged': "0:0:32",
        'is_complete': False,
        'tags': [],
        'comments': []
    }
    task = Task(new_task_dict)
    print(task.description)
    task.edit_description("Write Task-Manager Project")
    print(task.description)

    print(task.is_complete)
    task.mark_as_complete()
    print(task.is_complete)
    task.mark_as_complete()

    task.change_priority(5)
    print(task.priority)
    task.change_priority(3)
    print(task.priority)

    task.log_time(datetime.timedelta(minutes=32))
    print(task.time_logged)

    comment = {
        "author": "Jane",
        "text": "Better later than never."
    }
    task.add_comment(comment)
    print(task.comments)

    print(task)


if __name__ == '__main__':
    main()
