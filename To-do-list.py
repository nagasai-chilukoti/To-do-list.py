from tkinter import *

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass

window = Tk()
window.geometry("700x700")
window.title("To-Do List App")


label_title = Label(window,
                    text="To-Do List",
                    font=("Arial", 30, "bold"),
                    fg="navy",
                    bg="lightyellow",
                    width=20,
                    height=2,
                    relief=RAISED)
label_title.pack(pady=20)

label_add_task = Label(window,
                       text="Add Task:",
                       font=("Arial", 20, "bold"),
                       fg="purple")
label_add_task.place(x=10, y=150)

label_tasks = Label(window,
                    text="Tasks to do:  ",
                    font=("Arial", 20, "bold"),
                    fg="green")
label_tasks.place(x=10, y=300)


entry_task = Entry(window, font=("Arial", 16))
entry_task.place(x=170, y=150, width=300)

button_add_task = Button(window,
                         text="Add Task",
                         bg="orange",
                         fg="black",
                         font=("Arial", 14),
                         command=add_task,
                         relief=RAISED,
                         bd=3)
button_add_task.place(x=470, y=150, width=100)

button_delete_task = Button(window,
                            text="Delete Task",
                            bg="red",
                            fg="white",
                            font=("Arial", 14),
                            command=delete_task,
                            relief=RAISED,
                            bd=3)
button_delete_task.place(x=590, y=150, width=110)


listbox_tasks = Listbox(window, font=("Arial", 16), bg="lightgrey", selectbackground="lightblue")
listbox_tasks.place(x=200, y=300, width=540, height=300)


window.mainloop()
