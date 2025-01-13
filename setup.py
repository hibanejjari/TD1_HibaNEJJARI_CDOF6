# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:12:50 2025

@author: Nejjari
"""

# import necessary modules
import os

# define the todo app class
class todoapp:
    def __init__(self):
        self.tasks = []

    # display all tasks in the list
    def display_tasks(self):
        if not self.tasks:
            print("\nno tasks available.\n")
        else:
            print("\nyour tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "[x]" if task['completed'] else "[ ]"
                print(f"{idx}. {status} {task['description']}")

    # add a new task to the list
    def add_task(self):
        description = input("enter the task description: ").strip()
        if description:
            self.tasks.append({"description": description, "completed": False})
            print("task added successfully!\n")
        else:
            print("task description cannot be empty.\n")

    # delete a task from the list
    def delete_task(self):
        self.display_tasks()
        try:
            idx = int(input("enter the task number to delete: ")) - 1
            if 0 <= idx < len(self.tasks):
                removed_task = self.tasks.pop(idx)
                print(f"task '{removed_task['description']}' deleted successfully!\n")
            else:
                print("invalid task number.\n")
        except ValueError:
            print("please enter a valid number.\n")

    # mark a task as complete
    def complete_task(self):
        self.display_tasks()
        try:
            idx = int(input("enter the task number to mark as complete: ")) - 1
            if 0 <= idx < len(self.tasks):
                self.tasks[idx]['completed'] = True
                print("task marked as complete!\n")
            else:
                print("invalid task number.\n")
        except ValueError:
            print("please enter a valid number.\n")

    # main loop to run the app
    def run(self):
        while True:
            print("\nto-do list application")
            print("1. view tasks")
            print("2. add a task")
            print("3. delete a task")
            print("4. complete a task")
            print("5. exit")
            
            choice = input("choose an option: ").strip()

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                print("goodbye!")
                break
            else:
                print("invalid choice. please try again.\n")

# run the app if this script is executed directly
if __name__ == "__main__":
    app = todoapp()
    app.run()
