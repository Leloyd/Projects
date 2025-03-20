# Importing required modules
import json  # Importing json module for storing task data
from datetime import datetime  # Importing datetime to log task timestamps

# Task Manager Class
def validate_priority(priority):
    """Ensures priority is within the allowed range"""
    assert priority in ["Low", "Medium", "High"], "Invalid priority level!"

def validate_index(index, length):
    """Ensures index is within bounds"""
    assert 0 <= index < length, "Task index out of range!"

class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def add_task(self, description, priority="Medium"):
        """Adds a new task to the list"""
        validate_priority(priority)
        task = {"description": description, "priority": priority, "completed": False, "timestamp": datetime.now().isoformat()}
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, index):
        """Marks a task as completed"""
        validate_index(index, len(self.tasks))
        self.tasks[index]["completed"] = True
        print("Task marked as completed!")

    def delete_task(self, index):
        """Deletes a task from the list"""
        validate_index(index, len(self.tasks))
        del self.tasks[index]  # Deletes task from the list
        print("Task deleted successfully!")

    def display_tasks(self):
        """Displays all tasks"""
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['description']} [{task['priority']}] - {status} ({task['timestamp']})")

# Main function demonstrating Python keywords
def main():
    task_manager = TaskManager()  # Creates an instance of TaskManager

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task\n2. Complete Task\n3. Delete Task\n4. View Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            priority = input("Enter priority (Low, Medium, High): ")
            task_manager.add_task(desc, priority)
        elif choice == "2":
            index = int(input("Enter task index to complete: "))
            task_manager.complete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            task_manager.delete_task(index)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            break  # Exits the loop
        else:
            print("Invalid choice! Try again.")

    print("Exiting Task Manager.")

# Calling main function
if __name__ == "__main__":
    main()  # Runs the main function
