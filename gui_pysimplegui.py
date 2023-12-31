from datetime import datetime

import PySimpleGUI as sg

from todo import ToDo


# sg.main() # Update PySimpleGUI from GitHub
def update_listbox():
    td = ToDo()
    window.Element('_LISTBOX_').update(td.todo_list)


td = ToDo()

date_time_now = datetime.strftime(datetime.now(), '%b %d %H:%M:%S')

dt_label = sg.Text(date_time_now)
todo_label = sg.Text('Enter new To-Do:')
input_box = sg.InputText(key='_INPUT_', do_not_clear=False, size=49)
add_button = sg.Button('Add', size=11)
list_box = sg.Listbox(td.todo_list, key='_LISTBOX_', size=(48, 6),
                      enable_events=True, highlight_background_color='blue')
edit_button = sg.Button('Edit', size=5)
done_button = sg.Button('Done', size=5)
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
        td.add_to_list(todo)
        update_listbox()

    elif event == 'Done':
        try:
            todo = values['_LISTBOX_'][0]
            td.delete_todo(todo)
            update_listbox()

        except IndexError:
            sg.popup('Select an item first.', font=('Helvetica', 20),
                     no_titlebar=True, button_justification='center')

    elif event == 'Edit':
        try:
            if values['_INPUT_'] == '':
                sg.popup('To-do is empty.', font=('Helvetica', 20),
                         no_titlebar=True, button_justification='center')

            else:
                todo = values['_LISTBOX_'][0]
                new_todo = values['_INPUT_']
                td.edit_todo(todo, new_todo)
                update_listbox()

        except IndexError:
            sg.popup('Select an item first.', font=('Helvetica', 20),
                     no_titlebar=True, button_justification='center')

window.close()
