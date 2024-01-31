import datetime, os, sys

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/utils')
from file_operations import write_to_json, read_from_json

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from task import Task

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from space import Space

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from task_manager import TaskManager

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/classes')
from user import User

sys.path.append('/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/scripts')


def main():
    # program_started, user = starting_program()
    # if program_started:

    program_on = True

    while program_on:
        task_manager = TaskManager("program")

        action = input("""
1 - Show spaces and their tasks
2 - Assign me to do the task
3 - Add space
4 - Add task

7 - Quit program
    
What would you like to do now (choose a number): """)
        print()
        try:
            action = int(action)
        except ValueError:
            print("Invalid input. Please choose a number from a list provided.")
            continue

        if action == 1:
            spaces = task_manager._load_spaces()
            spaces_keys = spaces.keys()
            for key in spaces_keys:
                print(f"""{spaces[key]}""")
                for i in range(len(spaces[key].tasks)):
                    print(f"""  Task {i + 1}:
{str(spaces[key].tasks[i])}""")

        elif action == 2:
            assigning_to_space = input("In which space: ")
            spaces = task_manager._load_spaces()
            if assigning_to_space in spaces:
                assigning_to_task = input("Provide task description:")
                found_task = False
                tasks_to_check = spaces[assigning_to_space].tasks
                for i in range(len(tasks_to_check)):
                    if tasks_to_check[i].description == assigning_to_task:
                        tasks_to_check[i].assignee = user.name
                        print(f"Assigned {user.name} to task {tasks_to_check[i].description}")
                        spaces[assigning_to_space].save_to_database()
                        found_task = True
                if not found_task:
                    print("There is no such task in this space.")
            else:
                print("There's no such space. Please insert a valid one.")

        elif action == 3:
            spaces = task_manager._load_spaces()
            spaces_names = spaces.keys()
            new_space_name = input("Please insert new space name: ")
            new_space = task_manager.add_space(new_space_name)
            try:
                new_space.save_to_database()
            except AttributeError:
                pass

        elif action == 4:
            spaces = task_manager._load_spaces()
            spaces_names = list(spaces.keys())
            for i in range(len(spaces_names)):
                print(f"{i + 1} - {spaces_names[i]}")
            while True:
                space_selection = input("Please choose a number of a space that you'd like to add task to: ")
                try:
                    space_selection = int(space_selection)
                except ValueError:
                    print("Input must be a number from the list provided.")
                    continue
                if space_selection - 1 < len(spaces_names):
                    space_selected = spaces_names[space_selection - 1]
                    spaces[space_selected].add_task_from_input()
                    break
                else:
                    print("Input must be a number from the list provided.")

        elif action == 7:
            quit_program()
            break

        else:
            print("Invalid input. Please choose a number from a list provided.")


def starting_program():
    starting = True
    continue_program = True
    user = ''

    while starting:

        start = input("Do you want to log-in or register (login/register/quit): ")
        if start == "register":
            email = input("Please provide your email: ")
            password = input("Please provide your password: ")
            user = User(email, password)
            new_name = input("Provide your new name: ")
            user.set_name(new_name)
            print(f"Welcome in Task Manager {user.name}!")
            starting = False
            break

        elif start == "login":
            while True:
                email = input("Please provide your email: ")
                if email_in_database(email):
                    password = input("Please provide your password: ")
                    if password_checker(email, password):
                        name_container = get_name(email)
                        user = User(email, password)
                        user.name = name_container
                        print(f"Welcome back {email.split('@')[0]}")
                        starting = False
                        break
                    else:
                        decision = input("Password incorrect. Do you want to try again? (yes/no) ")
                        if decision == "yes":
                            continue
                        elif decision == "no":
                            break
                        else:
                            print("Input has to be from a list provided.")
                            continue
                else:
                    decision = input("Email not found. Do you want to try again? (yes/no) ")
                    if decision == "yes":
                        continue
                    elif decision == "no":
                        break
                    else:
                        print("Input has to be from a list provided.")
                        continue

        elif start == "quit":
            quit_program()
            continue_program = False
            break
        else:
            print("Input has to be from a list provided.")
            continue

    return continue_program, user


def quit_program():
    print("Thank you. See you again!")


def email_in_database(email):
    directory_path = '/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/data/users'
    users_directory = os.listdir(directory_path)
    users_list = [user.split('.')[0] for user in users_directory if user.split('.')[0] != '__init__']
    if email.split("@")[0] in users_list:
        return True
    else:
        return False


def password_checker(email, password_to_check):
    directory_path = '/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/data/users'
    user_path = f"{directory_path}/{email.split('@')[0]}.json"
    user_folder_data = read_from_json(user_path)
    if user_folder_data["password"] == password_to_check:
        return True
    else:
        return False


def get_name(email):
    directory_path = '/home/kuba/Desktop/bootcamp_2023-12-09/project-task-manager/src/data/users'
    user_path = f"{directory_path}/{email.split('@')[0]}.json"
    user_folder_data = read_from_json(user_path)
    return user_folder_data['name']


if __name__ == '__main__':
    main()
