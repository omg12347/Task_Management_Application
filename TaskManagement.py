class Task:
    def __init__(self, title, desc, last_date, priority):
        self.title = title
        self.last_date = last_date
        self.priority = priority
        self.desc = desc
        
class TaskGenius:
    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)
        print("✅ Congratulations! You've successfully added a new task to your TaskGenius list!")

    def delete(self, task_index):
        if task_index < len(self.task_list):
            del self.task_list[task_index]
            print("🗑️ Task deleted successfully! One less thing on your plate!")
        else:
            print("⚠️ Oops! The task index you entered is invalid. Please recheck and try again!")

    def update(self, task_index, updated_task):
        if task_index < len(self.task_list):
            self.task_list[task_index] = updated_task
            print("🚀 Task updated successfully! You're making great progress!")
        else:
            print("⚠️ Oops! That task index doesn't exist. Please double-check and try again!")
    
    def display(self):
        if self.task_list:
            print("📋 Your TaskGenius List:")
            for index, task in enumerate(self.task_list, start=1):
                print(f"Task {index}: {task.title}")
        else:
            print("🤷‍♂️ Oops! No tasks found. Time to add some genius tasks!")

# Create an instance of TaskGenius
task_genius = TaskGenius()

# Display options to the user
menu = """
--- TaskGenius Organizer ---
1. Add Task to list
2. Delete Task from list
3. Display Tasks from list 
4. Update Task 
5. Quit
"""

while True:
    print(menu)
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter task title: ")
        desc = input("Enter task description: ")
        last_date = input("Enter due date: ")
        priority = input("Enter task priority: ")
        task = Task(title, desc, last_date, priority)
        task_genius.add(task)

    elif choice == "2":
        task_genius.display()
        task_index = int(input("Enter the task index to delete: ")) - 1
        if task_index < len(task_genius.task_list):
            task_genius.delete(task_index)
        else:
            print("⚠️ Oops! Invalid task index. Please try again.")

    elif choice == "3":
        task_genius.display()
        
    elif choice == "4":
        task_genius.display()
        task_index = int(input("Enter the task index to update: ")) - 1
        if 0 <= task_index < len(task_genius.task_list):
            title = input("Enter updated task title: ")
            desc = input("Enter updated task description: ")
            last_date = input("Enter updated due date: ")
            priority = input("Enter updated task priority: ")
            updated_task = Task(title, desc, last_date, priority)
            task_genius.update(task_index, updated_task)
        else:
            print("⚠️ Oops! Invalid task index. Please try again.")
    
    elif choice == "5":
        print("👋 Exiting TaskGenius... Have a productive day ahead!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
