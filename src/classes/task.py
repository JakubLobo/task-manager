import datetime


class Task:
    priorities = [1, 2, 3]

    def __init__(self, task_data):
        self.description: str = task_data['description']
        self.assignee: str = task_data['assignee']
        self.due_date: datetime.date = datetime.datetime.strptime(task_data['due_date'], "%d/%m/%Y")
        self.priority: int = task_data['priority']
        self.time_logged: datetime.timedelta = self._change_time_to_timedelta(task_data['time_logged'])
        self.is_complete: bool = task_data['is_complete']
        self.tags: list[str] = task_data['tags']
        self.comments: list[dict[str, str]] = task_data['comments']

    @staticmethod
    def _change_time_to_timedelta(time):
        datetime_time: datetime = datetime.datetime.strptime(time, "%H:%M:%S")
        timedelta_time = datetime.timedelta(hours=datetime_time.hour,
                                            minutes=datetime_time.minute,
                                            seconds=datetime_time.second)
        return timedelta_time

    @staticmethod
    def validate_completion(status):
        if status:
            return 'Done'
        return "To do"

    def __str__(self):
        return f"""Description: {self.description}
Status: {self.validate_completion(self.is_complete)}
Assignee: {self.assignee}
Due_date: {self.due_date}
Priority: {self.priority}
Tags: {self.tags}
Comments: {self.comments}"""

    def edit_description(self, new_description):
        if isinstance(new_description, str):
            self.description = new_description
        else:
            print("Given description is not a string.")

    def mark_as_complete(self):
        if self.is_complete is False:
            self.is_complete = True
        else:
            print("Given task is already completed.")

    def change_priority(self, new_priority):
        if new_priority in Task.priorities:
            self.priority = new_priority
        else:
            print("Priority has to be 1, 2 or 3.")

    def log_time(self, time_frame):
        if isinstance(time_frame, datetime.timedelta):
            self.time_logged += time_frame

    @staticmethod
    def _validate_comment(given_comment):
        if isinstance(given_comment, dict) \
                and isinstance(given_comment['author'], str) \
                and isinstance(given_comment['text'], str):
            return True
        return False

    def add_comment(self, new_comment):
        if self._validate_comment(new_comment):
            self.comments.append(new_comment)
