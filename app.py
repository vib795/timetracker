import tkinter as tk
import time

def start_task():
    global start_time, current_task
    start_time = time.time()
    current_task = task_entry.get()
    status_label.config(text=f"Task '{current_task}' is running...")
    task_entry.config(state='disabled')
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_task():
    global total_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    tasks[current_task] = elapsed_time
    total_time += elapsed_time
    update_task_list()
    update_total_time_label()
    task_entry.delete(0, tk.END)
    task_entry.config(state='normal')
    start_button.config(state='normal')
    stop_button.config(state='disabled')
    status_label.config(text="No task is running.")

def update_task_list():
    tasks_listbox.delete(0, tk.END)
    for task, elapsed_time in tasks.items():
        tasks_listbox.insert(tk.END, f"Task: {task} - Time spent: {elapsed_time:.2f} seconds")

def update_total_time_label():
    total_time_label.config(text=f"Total time spent today: {total_time:.2f} seconds")

def close_app():
    root.destroy()

# Initialize Tkinter
root = tk.Tk()
root.title("Task Tracker")
root.geometry("500x400")

tasks = {}
current_task = None
total_time = 0.0

# Widgets
task_label = tk.Label(root, text="Enter the task you're starting:")
task_label.pack()

task_entry = tk.Entry(root, width=50)
task_entry.pack()

start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack()

stop_button = tk.Button(root, text="Stop Task", command=stop_task, state='disabled')
stop_button.pack()

status_label = tk.Label(root, text="No task is running.")
status_label.pack()

listbox_frame = tk.Frame(root)
listbox_frame.pack()

tasks_listbox = tk.Listbox(listbox_frame, width=50, height=10)
tasks_listbox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=tasks_listbox.yview)
scrollbar.pack(side="right", fill="y")

tasks_listbox.config(yscrollcommand=scrollbar.set)

total_time_label = tk.Label(root, text="Total time spent today: 0.0 seconds")
total_time_label.pack()

close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack()

# Start the application
root.mainloop()
