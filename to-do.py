import tkinter as tk

task_labels = []
checkboxes = []
delete_buttons = []

row_index = 5


def add_task(clear_entry=True):
    global task_labels, row_index, checkboxes, delete_buttons
    row_index = 5  # reset to starting row

    # Clear old labels
    for widget in task_labels + checkboxes + delete_buttons:
        widget.destroy()

    task_labels.clear()
    checkboxes.clear()
    delete_buttons.clear()

    # get new task
    task_name = entry.get()
    if task_name:  # Only proceed if task_name is not empty
        tasks.append({"task": task_name, "completed": False})

    for i, task in enumerate(tasks):
        # create checkbox and task label
        check_task = tk.Checkbutton(root, onvalue=0)
        new_label = tk.Label(root, text=task["task"])
        del_button = tk.Button(root, text="X", command=lambda i=i: del_task(i))

        # grid method to arrange check and label
        check_task.grid(row=row_index, column=0, pady=2, sticky='nsew')
        new_label.grid(row=row_index, column=1, pady=2, sticky='nsew')
        del_button.grid(row=row_index, column=2, pady=2, sticky='nsew')

        row_index += 1
        task_labels.append(new_label)
        checkboxes.append(check_task)
        delete_buttons.append(del_button)

    if clear_entry:
        entry.delete(0, tk.END)


def del_task(index):
    del tasks[index]
    add_task(False)  # Refresh the display

# Initialise main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# initialise task list
tasks = []

# entry widget
entry = tk.Entry(root)
entry.grid(row=2, column=0, columnspan=3, sticky='ew')

# enter button
add_button = tk.Button(root, text="Add task", command=add_task)
add_button.grid(row=3, column=0, columnspan=3, sticky='ew')

# delete button
del_button = tk.Button(root, text="X", command=del_task)

# header
# Create and style the header
header = tk.Label(root, text="My To-Do List", font=("Helvetica", 16), bg="lightblue", fg="white")
header.grid(row=0, column=0, columnspan=3, sticky='ew')

# image
# Import the image
image = tk.Label(root, text="ᕦ(⩾﹏⩽)ᕥ", font=("Courier", 24))
# Create a Label widget with the image
image.grid(row=1, column=0, columnspan=3, sticky='ew')

# main loop
root.mainloop()
