filepath = 'todos.txt'


def get_todos():
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data


def overwrite_todos(data):
    with open(filepath, 'w') as file:
        file.writelines(data)
