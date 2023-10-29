import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from todo import ToDo

BG_COLOR = '#2C3333'
FG_COLOR = "#E7F6F2"
FONT = font = ('Arial', 15, 'normal')

now = datetime.now().strftime("%b %d, %Y")

td = ToDo()


def close_win(top):
    top.destroy()
    return


def edit_popup():
    top = tk.Toplevel(root)
    top.config(bg=BG_COLOR, padx=20, pady=20)

    label = tk.Label(top, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                     text="Enter new to do:")
    label.grid(row=0, column=0)

    new_entry = tk.Entry(top, width=40, bg=FG_COLOR, font=FONT)
    new_entry.grid(row=0, column=1)

    frame = tk.Frame(top)
    frame.config(bg=BG_COLOR, pady=10)
    frame.grid(columnspan=2)

    ok_bttn = tk.Button(frame, width=8, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                        text="OK",
                        command=lambda: [edit(new_entry.get()), close_win(top)])  # Bind two functions
    ok_bttn.grid(row=1, column=0, padx=5)

    cancel_button = tk.Button(frame, width=8, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                              text="Cancel",
                              command=lambda: close_win(top))
    cancel_button.grid(row=1, column=1)


def add_todo(new_todo):
    if new_todo in td.todo_list:
        messagebox.showerror(message="Task already in your to do.")
    else:
        td.add_to_list(new_todo)
        todo_entry.delete(0, 'end')
        list_box.insert(len(td.todo_list), new_todo)


def edit(new_todo):
    try:
        selected_todo = ""
        for i in list_box.curselection():
            selected_todo = list_box.get(i)
        td.edit_todo(selected_todo, new_todo)
        list_box.delete(0, 'end')
        for i, todo in enumerate(td.todo_list):
            list_box.insert(i, todo)

    except ValueError:
        messagebox.showerror(message="Select a task.")


def delete():
    try:
        selected_todo = ""
        for i in list_box.curselection():
            selected_todo = list_box.get(i)
        td.delete_todo(selected_todo)
        list_box.delete(0, 'end')
        for i, todo in enumerate(td.todo_list):
            list_box.insert(i, todo)

    except ValueError:
        messagebox.showerror(message="Select a task.")


root = tk.Tk()
root.title("What To Do")
root.config(bg=BG_COLOR, padx=20, pady=20)

# Displays current date and prompt
time = tk.Label(root, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT, text=now)
time.grid(row=0, column=2, sticky='e')
label = tk.Label(root, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                 text="What do you need to do today?")
label.grid(row=1, column=0, sticky='w')

# Create entry
todo_entry = tk.Entry(root, width=50, bg=FG_COLOR, font=FONT)
todo_entry.grid(row=2, column=0)
todo_entry.focus()

# Create Buttons
add_bttn = tk.Button(root, width=10, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                     text="Add", command=lambda: add_todo(todo_entry.get()))
add_bttn.grid(row=2, column=2, padx=10, pady=5)

edit_bttn = tk.Button(root, width=10, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                      text="Edit", command=edit_popup)
edit_bttn.grid(row=3, column=2, padx=10, pady=5, sticky='n')

del_bttn = tk.Button(root, width=10, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=FONT,
                     text="Delete", command=delete)
del_bttn.grid(row=3, column=2, padx=10)

# Create a List Box
list_box = tk.Listbox(root, width=50, bg=FG_COLOR, font=FONT, activestyle='dotbox')
list_box.grid(row=3, column=0, rowspan=2)

# Populate List Box
for i, todo in enumerate(td.todo_list):
    list_box.insert(i, todo)

root.mainloop()
