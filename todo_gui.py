from modules import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo...",
                         key="todo",
                         font=('Helvetica', 12))
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True, size=[44, 10])
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10)

window = sg.Window('TODO App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    # Returns a tuple(event, values{key:value}).
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%H:%S"))

    match event:
        case "Add":
            # Opening a file in 'r' mode returns a list.
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # It refreshes the window containing 'todos' and updates the list.
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                # Does the same as above
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 10))

        case "todos":
            # It updates the window containing 'todo' with the user select values.
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            try:
                todos = functions.get_todos()
                todo_to_complete = todos.index(values['todos'][0])
                todos.pop(todo_to_complete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 10))

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()