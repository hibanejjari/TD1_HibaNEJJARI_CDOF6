# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:12:50 2025

@author: Nejjari
"""

# Import necessary modules
import os

# Define the TodoApp class to handle the to-do list operations
class TodoApp:
    def __init__(self, file_name="tasks.txt"):
        # Initialize the app with an empty task list and the default file name for saving tasks
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()  # Load previously saved tasks at startup

    # Load tasks from the file at the start of the application
    def load_tasks(self):
        # Check if the file exists and load tasks from it
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                # Read each line, split it by '||' to get task description and completion status
                for line in file:
                    description, completed = line.strip().split("||")
                    # Append the task as a dictionary to the tasks list
                    self.tasks.append({
                        "description": description,
                        "completed": completed == "True"  # Convert the 'True'/'False' string to boolean
                    })
            print(f"Loaded {len(self.tasks)} task(s) from {self.file_name}.\n")
        else:
            # If no file is found, print a message and start with an empty list
            print("No saved tasks found. Starting fresh!\n")

    # Save all current tasks to the file
    def save_tasks(self):
        # Open the file in write mode and save each task to the file
        with open(self.file_name, "w") as file:
            for task in self.tasks:
                # Write task description and completion status separated by '||'
                file.write(f"{task['description']}||{task['completed']}\n")
        print("Tasks saved successfully!\n")

    # Display all tasks to the user
    def display_tasks(self):
        # If no tasks exist, print a message indicating the list is empty
        if not self.tasks:
            print("\nNo tasks available.\n")
        else:
            # Otherwise, display all tasks with their status
            print("\nYour tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                # Display a checked box if the task is completed, or an empty box if not
                status = "[x]" if task['completed'] else "[ ]"
                print(f"{idx}. {status} {task['description']}")

    # Add a new task to the list
    def add_task(self):
        # Ask the user to enter a task description
        description = input("Enter the task description: ").strip()
        if description:  # If the description is not empty
            # Append the new task as a dictionary with a 'False' completion status
            self.tasks.append({"description": description, "completed": False})
            self.save_tasks()  # Save the updated list of tasks to the file
            print("Task added successfully!\n")
        else:
            # If no description is entered, print an error message
            print("Task description cannot be empty.\n")

    # Delete a task from the list
    def delete_task(self):
        # Display current tasks before asking the user to delete one
        self.display_tasks()
        try:
            # Ask the user to input the task number to delete
            idx = int(input("Enter the task number to delete: ")) - 1
            # Check if the entered index is valid
            if 0 <= idx < len(self.tasks):
                # Remove the task from the list and save the updated list
                removed_task = self.tasks.pop(idx)
                self.save_tasks()
                print(f"Task '{removed_task['description']}' deleted successfully!\n")
            else:
                # If the index is invalid, print an error message
                print("Invalid task number.\n")
        except ValueError:
            # Handle the case where the user enters a non-numeric value
            print("Please enter a valid number.\n")

    # Mark a task as completed
    def complete_task(self):
        # Display current tasks before asking the user to mark one as complete
        self.display_tasks()
        try:
            # Ask the user to input the task number to mark as complete
            idx = int(input("Enter the task number to mark as complete: ")) - 1
            # Check if the entered index is valid
            if 0 <= idx < len(self.tasks):
                # Change the 'completed' status of the task to True and save the updated list
                self.tasks[idx]['completed'] = True
                self.save_tasks()
                print("Task marked as complete!\n")
            else:
                # If the index is invalid, print an error message
                print("Invalid task number.\n")
        except ValueError:
            # Handle the case where the user enters a non-numeric value
            print("Please enter a valid number.\n")

    # Main loop to run the app
    def run(self):
        while True:
            # Display the menu options to the user
            print("\nTo-Do List Application")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Delete a task")
            print("4. Complete a task")
            print("5. Exit")
            
            # Ask the user to choose an option
            choice = input("Choose an option: ").strip()

            # Perform the corresponding action based on the user's choice
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
                # If the user enters an invalid choice, print an error message
                print("Invalid choice. Please try again.\n")

# Run the app if this script is executed directly
if __name__ == "__main__":
    app = TodoApp()  # Create an instance of the TodoApp class
    app.run()  # Start the app
