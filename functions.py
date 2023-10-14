filepath = 'todos.txt'


def get_todos():
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data


def todos_list():
    data = get_todos()
    new_list = [todo.strip('\n') for todo in data]
    return new_list


def overwrite_todos(data):
    new_data = [item + '\n' for item in data]
    with open(filepath, 'w') as file:
        file.writelines(new_data)
