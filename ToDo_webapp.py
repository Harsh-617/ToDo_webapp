
def get_todos(filepath = r"TODO_list"):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath= r"TODO_list"):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


import streamlit as st

todos = get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""  #clears the input box

st.title("My ToDo App")
st.subheader("This is my daily to-do app")
st.write("This app increases your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #print(checkbox)
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="enter a todo", placeholder="add a new todo", on_change=add_todo, key="new_todo")

# print('hello')
# st.session_state