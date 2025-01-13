# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:12:50 2025

@author: Nejjari
"""

# todo_list_app.py

# import necessary modules
import os

# define the todo app class
class TodoApp:
    def __init__(self, file_name="tasks.txt"):
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()

    # Load tasks from file at startup
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                for line in file:
                    description, completed = line.strip().split("||")
                    self.tasks.append({
                        "description": description,
                        "completed": completed == "True"
                    })
            print(f"Loaded {len(self.tasks)} task(s) from {self.file_name}.\n")
        else:
            print("No saved tasks found. Starting fresh!\n")

    # Save tasks to the file
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            for task in self.tasks:
                file.write(f"{task['description']}||{task['completed']}\n")
        print("Tasks saved successfully!\n")

    # display all tasks in the list
    def display_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
        else:
            print("\nYour tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "[x]" if task['completed'] else "[ ]"
                print(f"{idx}. {status} {task['description']}")

    # add a new task to the list
    def add_task(self):
        description = input("Enter the task description: ").strip()
        if description:
            self.tasks.append({"description": description, "completed": False})
            self.save_tasks()
            print("Task added successfully!\n")
        else:
            print("Task description cannot be empty.\n")

    # delete a task from the list
    def delete_task(self):
        self.display_tasks()
        try:
            idx = int(input("Enter the task number to delete: ")) - 1
            if 0 <= idx < len(self.tasks):
                removed_task = self.tasks.pop(idx)
                self.save_tasks()
                print(f"Task '{removed_task['description']}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

    # mark a task as complete
    def complete_task(self):
        self.display_tasks()
        try:
            idx = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= idx < len(self.tasks):
                self.tasks[idx]['completed'] = True
                self.save_tasks()
                print("Task marked as complete!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

    # main loop to run the app
    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Delete a task")
            print("4. Complete a task")
            print("5. Exit")
            
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

# run the app if this script is executed directly
if __name__ == "__main__":
    app = TodoApp()
    app.run()