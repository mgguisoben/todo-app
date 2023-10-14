from functions import get_todos, overwrite_todos
from datetime import datetime
import PySimpleGUI as sg

date_time_now = datetime.strftime(datetime.now(), '%b %d %H:%M:%S')

layout = [ [sg.Text(date_time_now)],
           [sg.Text('Enter new To-Do:')],
           [sg.InputText(do_not_clear=False), sg.Button('Add', size=10)], # input field auto clear
           [sg.Text("more text"), [sg.Button('Edit'), sg.Button('Done')]],
           [sg.Button('Quit', size=10)]
         ]

window = sg.Window('My TO-DO App', layout)

while True:

    events, values = window.read()

    if events == sg.WIN_CLOSED or events == 'Quit':
        break

window.close()