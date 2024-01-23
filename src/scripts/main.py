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


def main():

    program_on = True

    while program_on:

        start = input("Do you want to log-in or register (login/register/quit): ")
        if start == "register":
            email = input("Please provide your email: ")
            password = input("Please provide your password: ")
            new_user = User(email, password)
            new_name = input("Provide your new name: ")
            new_user.set_name(new_name)

        elif start == "login":
            while True:
                email = input("Please provide your email: ")
                if email_in_database(email):
                    password = input("Please provide your password: ")
                    if password_checker(email, password):
                        print(f"Welcome back {email.split('@')[0]}")
                        break
                    else:
                        decision = input("Password incorrect. Do you want to try again? (yes/no) ")
                        if decision == "yes":
                            continue
                        elif decision == "no":
                            break
                        else:
                            print("Input has to be a number from a list provided.")
                            continue
                else:
                    decision = input("Email not found. Do you want to try again? (yes/no) ")
                    if decision == "yes":
                        continue
                    elif decision == "no":
                        break
                    else:
                        print("Input has to be a number from a list provided.")
                        continue

        elif start == "quit":
            quit_program()
            break
        else:
            print("Input has to be a number from a list provided.")
            continue


if __name__ == '__main__':
    main()
