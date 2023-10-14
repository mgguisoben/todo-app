from functions import get_todos, todos_list, overwrite_todos
from datetime import datetime
import PySimpleGUI as sg

date_time_now = datetime.strftime(datetime.now(), '%b %d %H:%M:%S')
todos = todos_list()
print(todos)

layout = [ [sg.Text(date_time_now)],
           [sg.Text('Enter new To-Do:')],
           [sg.InputText(key='_INPUT_' ,do_not_clear=False, size=50), sg.Button('Add', size=10)], # input field auto clear
           [sg.Listbox(key='_LISTBOX_', values=todos, size=(48, 6), enable_events=True),
            sg.Button('Edit', size=4), sg.Button('Done', size=4)],
           [sg.Button('Quit', size=10)]
         ]

window = sg.Window('My TO-DO App').Layout(layout)

while True:

    event, values = window.read()
    window.Element('_LISTBOX_').update((todos))

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'Add':
        todo = values['_INPUT_']
        todos.append(todo)
        overwrite_todos(todos)
        window.Element('_LISTBOX_').update((todos))

    if event == '_LISTBOX_' and len(values['_LISTBOX_']):
        window.Element('_INPUT_').update(values['_LISTBOX_'])

    if event == 'Done':
        try:
            todo = values['_INPUT_'][2:-3]
            index = todos.index(todo)
            todos.pop(index)
            window.Element('_LISTBOX_').update((todos))
        except ValueError:
            continue

    # if event == 'Edit':
    #     window.Element('_INPUT_').update(values['_LISTBOX_'])
    #     sg.Popup('Edit To-DO', values['_INPUT_'])


window.close()