tasks=[]
while True: #infinite loop
    print("\n---To-Do List Menu ---")
    print("1. Add a task")
    print("2. View task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option(1-4):")

    if choice =="1":
        task = input("Enter the task to add:")
        tasks.append(task)
        print("Task " + task + " added!")
    elif choice =="2":
        for i in tasks:
            print(i)
    elif choice =="3":
        task = input("Enter the name of the task you want to remove: ")
        tasks.remove(task)
        print("task " + task + " removed!")
    elif choice =="4":
        print("Exiting the program Goodbye!!")
        break

#ASSIGNMENT
movies = []
while True:
    print("\n--- Movie Collection Menu ---")
    print("1. View Movies")
    print("2. Add a movie")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        for movie in movies:
            print(movie)
    elif choice == "2":
        movie = input("Enter the movie to add: ")
        movies.append(movie)
        print("Movie " + movie + " added!")
    elif choice == "3":
        print("Exiting the program. Goodbye!!")
        break
