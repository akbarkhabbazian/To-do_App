import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box , add_button]],
                   font=("Helvetica", 20))

window.read()
print("Hello")
window.close()