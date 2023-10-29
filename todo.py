FILEPATH = 'todos.txt'


class ToDo:

    def __init__(self):
        self.todo_list = []
        self.get_todo_list()

    def get_todo_list(self):
        try:
            with open(FILEPATH, 'r') as file:
                data = file.readlines()
                for todo in data:
                    self.todo_list.append(todo.strip())
            return self.todo_list
        except FileNotFoundError:
            with open(FILEPATH, 'w') as file:
                return None

    def add_to_list(self, todo):
        with open(FILEPATH, 'a') as file:
            file.writelines(todo + "\n")

    def edit_todo(self, todo, new_todo):
        i = self.todo_list.index(todo)
        self.todo_list[i] = new_todo
        new_list = [todo + "\n" for todo in self.todo_list]
        with open(FILEPATH, 'w') as file:
            file.writelines(new_list)

    def delete_todo(self, todo):
        i = self.todo_list.index(todo)
        self.todo_list.pop(i)
        new_list = [todo + "\n" for todo in self.todo_list]
        with open(FILEPATH, 'w') as file:
            file.writelines(new_list)