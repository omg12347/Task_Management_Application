import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def update_task(self, task_index, updated_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = updated_task


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return User(username, password)

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return users.get(username, None) if users else None

def add_task(user):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = Task(title, description, due_date)
    user.add_task(task)
    print("Task added successfully.")

def delete_task(user):
    if not user.tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(user.tasks):
        print(f"{index + 1}. {task.title} (Due: {task.due_date})")

    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(user.tasks):
        user.delete_task(task_index)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def update_task(user):
    if not user.tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(user.tasks):
        print(f"{index + 1}. {task.title} (Due: {task.due_date})")

    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(user.tasks):
        title = input("Enter updated task title: ")
        description = input("Enter updated task description: ")
        due_date = input("Enter updated due date (YYYY-MM-DD): ")

        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        updated_task = Task(title, description, due_date)
        user.update_task(task_index, updated_task)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def task_reminder(user):
    today = datetime.datetime.now().date()
    reminder_tasks = [task for task in user.tasks if task.due_date.date() == today]

    print("🔔 Today's Task Reminder 🔔")
    for task in reminder_tasks:
        print(f"Task: {task.title} (Due: {task.due_date})")


def main():
    users = {}
    user = None

    while True:
        print("\n--- DAILY TASK SCHEDULER ---")
        print("1. Register")
        print("2. Login")
        print("3. Add Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Task Reminder")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = register()
            users[user.username] = user
            print("Registration successful!")

        elif choice == "2":
            user = login(users)
            if user:
                print(f"Welcome, {user.username}!")
            else:
                print("Invalid username or password. Please try again.")

        elif choice == "3":
            if user:
                add_task(user)
            else:
                print("Please log in to add a task.")

        elif choice == "4":
            if user:
                update_task(user)
            else:
                print("Please log in to update a task.")

        elif choice == "5":
            if user:
                delete_task(user)
            else:
                print("Please log in to delete a task.")

        elif choice == "6":
            if user:
                task_reminder(user)
            else:
                print("Please log in to see the task reminder.")

        elif choice == "7":
            print("Exiting the Daily Task Scheduler...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
