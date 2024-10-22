import json
from typing import List, Dict
from datetime import datetime


class Task:
    def __init__(self, description: str):
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Task":
        task = cls(data["description"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task


class TodoList:
    def __init__(self):
        self.tasks: List[Task] = []
        self.load_tasks()

    def add_task(self, description: str) -> None:
        self.tasks.append(Task(description))
        self.save_tasks()

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task.completed else " "
                print(f"{i}. [{status}] {task.description}")

    def mark_completed(self, index: int) -> None:
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, index: int) -> None:
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            self.save_tasks()
            print("Task deleted.")
        else:
            print("Invalid task number.")

    def save_tasks(self) -> None:
        with open("tasks.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self) -> None:
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []


def main():
    todo_list = TodoList()

    while True:
        print("\n--- Todo List Menu ---")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
