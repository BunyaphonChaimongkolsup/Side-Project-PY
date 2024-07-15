class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append({"task":task, "completed":False})
        print(f"Added task: {task}")
        
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Completed task: {self.tasks[index]['task']}")
        else:
            print("Invalid task number.")

    def delete_task(self,index):
        if 0 <= index < len(self.tasks):
            remove_task = self.tasks.pop(index)
            print(f"Deleted task: {remove_task['task']}")
        else:
            print("Invalid task number.")
        
    def show_task(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not completed"
                print(f"{i+1}. {task['task']} - {status}")
                
def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List Menu\n1. Add task\n2. Complete task\n3. Delete task\n4. Show tasks\n5. Exit")
        
        choice = input("Choose an option : ")
        
        if choice == '1':
            task = input("Enter the task : ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                index = int(input("Enter the task number to complete : ")) - 1
                todo_list.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                index = int(input("Enter the task number to delete : ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo_list.show_task()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")
            
if __name__ == "__main__":
    main()