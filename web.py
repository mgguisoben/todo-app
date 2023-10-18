from functions import todos_list
import streamlit as st

todos = todos_list()

st.title('To-Do Web App')
st.subheader('To-do web app using streamlit')
st.write('Thing you need to do.')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add a to-do')

st.button(label='Add')