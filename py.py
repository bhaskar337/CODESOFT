def main():
    tasks = []

    while True:
        print("/n$$$$$$ To-Do List $$$$$$")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_task = int(input("How may task you want to add: "))

            for i in range(n_task):
                task = input("Enter the task: ")
                tasks.append({"task": task, "complete": False}) 
                print("Task added")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "complete" if task["complete"] else "Not complete"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["complete"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()    
