from functions import todos_list, overwrite_todos
from datetime import datetime
import PySimpleGUI as sg

date_time_now = datetime.strftime(datetime.now(), '%b %d %H:%M:%S')
todos = todos_list()

dt_label = sg.Text(date_time_now)
todo_label = sg.Text('Enter new To-Do:')
input_box = sg.InputText(key='_INPUT_', do_not_clear=False, size=50)
add_button = sg.Button('Add', size=10)
list_box = sg.Listbox(todos, key='_LISTBOX_', size=(48, 6), enable_events=True, highlight_background_color='blue')
edit_button = sg.Button('Edit', size=4)
done_button = sg.Button('Done', size=4)
quit_button = sg.Button('Quit', size=10)

layout = [[dt_label],
          [todo_label],
          [input_box, add_button],
          [list_box, edit_button, done_button],
          [quit_button]]

window = sg.Window('My TO-DO App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    elif event == 'Add':
        todo = values['_INPUT_']
        todos.append(todo)
        print(todos)
        overwrite_todos(todos)
        window.Element('_LISTBOX_').update(todos)

    elif event == 'Done':
        todo = values['_LISTBOX_'][0]
        index = todos.index(todo)
        todos.pop(index)
        overwrite_todos(todos)
        window.Element('_LISTBOX_').update(todos)

    elif event == 'Edit':
        todo = values['_LISTBOX_'][0]
        new_todo = values['_INPUT_']
        index = todos.index(todo)
        todos[index] = new_todo
        overwrite_todos(todos)
        window.Element('_LISTBOX_').update(todos)

window.close()
