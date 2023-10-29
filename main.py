import datetime as dt

from todo import ToDo

now = dt.datetime.now().strftime('%b %d %H:%M:%S')

while True:
    print(f"Today is {now}")
    user_action = input("Type show, add, edit, done, or exit: ").lower()

    if user_action.startswith('add'):
        todo = input("Enter to do: ").capitalize()
        td = ToDo()
        td.add_to_list(todo)

    elif user_action.startswith('show'):
        print("To-Do's:")
        td = ToDo()
        for index, item in enumerate(td.todo_list):
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            td = ToDo()
            index = int(input(f"Choose a to 1-{len(td.todo_list)}: "))
            todo = input("Enter a new to do: ").capitalize()
            td.edit_todo(td.todo_list[index - 1], todo)

        except IndexError:
            print("ERROR: To do not found.")
            continue

    elif user_action.startswith('done'):
        try:
            td = ToDo()
            index = int(input(f"Done with 1-{len(td.todo_list)}: "))
            todo = td.todo_list[index - 1]
            td.delete_todo(todo)

        except IndexError:
            print("ERROR: To-do not found.")
            continue

        except ValueError:
            print("You entered an unknown command.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("You entered an unknown command.")

print("Bye!")
