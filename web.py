from functions import todos_list, overwrite_todos
import streamlit as st

todos = todos_list()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    overwrite_todos(todos)


st.title('TODO')
st.subheader('Minimalist to-do web app:')
st.write('Thing you need to do:')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        overwrite_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='What do you need to do?', placeholder='Add a to-do',
              key='new_todo', on_change=add_todo)
