import tkinter
import tkinter.messagebox
import pickle
from tkinter import *


root = tkinter.Tk()
root.title("To-Do List")

# Function to add task and clear text box, only if a task is entered
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Function for if enter key is pressed to enter task
def enter_key(enter):
    add_task()

# Function for if delete key is pressed to delete task
def delete_key(delete):
    delete_task()

# Function to delete task, only if a selection is made
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to load tasks, only if a save file has been found (tasks.dat file)
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No save file found.")

# Function to save tasks to tasks.dat file
def save_tasks():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Function to mark task as complete, only if a selection is made
def mark_complete():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg':'green'})
        listbox_tasks.itemconfig(task_index, {'fg':'white'})
        listbox_tasks.selection_clear(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to mark task as incomplete, only if a selection is made
def mark_incomplete():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg':'white'})
        listbox_tasks.itemconfig(task_index, {'fg':'black'})
        listbox_tasks.selection_clear(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to mark task as inprogress, only if a selection is made
def mark_inprogress():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg':'yellow'})
        listbox_tasks.itemconfig(task_index, {'fg':'black'})
        listbox_tasks.selection_clear(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


# Create GUI
# Create frame to hold listbox and scroll bar next to it
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

# Create list box
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

# Create scroll bar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# Add functionality to the scrollbar
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Text box to enter tasks
entry_task = tkinter.Entry(root, width=52)
entry_task.pack()

# Use enter key to submit task
root.bind('<Return>', enter_key)

# Use delete key to delete task
root.bind('<Delete>', delete_key)

# Button to add task
button_add_task = tkinter.Button(root, text="Add Task", width=43, command=add_task)
button_add_task.pack()

# Button to delete task
button_delete_task = tkinter.Button(root, text="Delete Task", width=43, command=delete_task)
button_delete_task.pack()

# Create frame to hold buttons to mark tasks complete or incomplete
frame_mark_tasks = tkinter.Frame(root)
frame_mark_tasks.pack()

# Button to mark tasks as complete
button_mark_complete = tkinter.Button(frame_mark_tasks, text="Mark Complete", width=14, command=mark_complete)
button_mark_complete.pack(side=tkinter.LEFT)

# Button to mark completed tasks as incomplete
button_mark_incomplete = tkinter.Button(frame_mark_tasks, text="Mark Incomplete", width=14, command=mark_incomplete)
button_mark_incomplete.pack(side=tkinter.RIGHT)

# Button to mark completed tasks as in progress
button_mark_inprogress = tkinter.Button(frame_mark_tasks, text="Mark in Progress", width=12, command=mark_inprogress)
button_mark_inprogress.pack()

# Button to load tasks
button_load_tasks = tkinter.Button(root, text="Load Tasks", width=43, command=load_tasks)
button_load_tasks.pack()

# Button to save tasks
button_save_tasks = tkinter.Button(root, text="Save Tasks", width=43, command=save_tasks)
button_save_tasks.pack()

root.mainloop()