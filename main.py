from functions import get_todos, overwrite_todos
from datetime import datetime

date_time_now = datetime.strftime(datetime.now(), '%b %d %H:%M:%S')


class ToDo:

    while True:
        print(f"Today is {date_time_now}")
        todos = get_todos()
        user_action = input("Type show, add, edit, done, or exit: ").lower()

        if user_action.startswith('add'):
            todo = input("Enter to do: ").capitalize()

            todos.append(todo + '\n')
            overwrite_todos(todos)

        elif user_action.startswith('show'):
            print("To-Do's:")
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")

        elif user_action.startswith('edit'):
            try:
                index = int(input(f"Choose a to 1-{len(todos)}: "))
                todo = input("Enter a new to do: ").capitalize()
                todos[index - 1] = todo + '\n'
                overwrite_todos(todos)

            except IndexError:
                print("ERROR: To-do not found.")
                continue

        elif user_action.startswith('done'):
            try:
                index = int(input(f"Done with 1-{len(todos)}: "))
                todos.pop(index - 1)

                overwrite_todos(todos)

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


if __name__ == '__main__':
    todo_start = ToDo()
