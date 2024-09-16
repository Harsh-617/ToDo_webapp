import streamlit as st

import sys
sys.path.append('..')
from demo import TODO_functions
todos = TODO_functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    TODO_functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my daily to-do app")
st.write("This app increases your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #print(checkbox)
        todos.pop(index)
        TODO_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="enter a todo", placeholder="add a new todo", on_change=add_todo, key="new_todo")

# print('hello')
# st.session_state