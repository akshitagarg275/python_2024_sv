'''
sqlite -> It contain rows and columns
C -> Create
R -> Read
U -> Update
D -> Delete
'''
from todo_helper import create_table, read_todo, add_todo, update_todo, delete_task,close_connection

def main():
    run = 1 
    create_table()

    while run:
        print("Press 1: To read data")
        print("Press 2: To add data")
        print("Press 3: To update data")
        print("Press 4: To delete data")
        print("Press 5: To exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            read_todo()
        elif ch == "2":
            todo = input("Enter the todo: ")
            add_todo(todo)
        elif ch == "3":
            id = int(input("Enter the ID of the todo to be updated"))
            new_todo = input("Enter the todo to be updated")
            update_todo(id, new_todo)
        elif ch == "4":
            id = int(input("Enter the ID of the todo to be deleted"))
            delete_task(id)
        
        elif ch == "5":
            run = 0
    

    close_connection()



if __name__ == '__main__':
    main()