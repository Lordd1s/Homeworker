import tkinter as tk

def start_timer():
    global elapsed_time, timer_running
    timer_running = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    update_timer()

def stop_timer():
    global timer_running
    timer_running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def update_timer():
    global elapsed_time, timer_running
    if timer_running:
        elapsed_time += 1
        time_var.set("{:02d}:{:02d}:{:02d}".format(elapsed_time // 3600, (elapsed_time // 60) % 60, elapsed_time % 60))
        root.after(1000, update_timer)

root = tk.Tk()

elapsed_time = 0
timer_running = False

time_var = tk.StringVar(value="00:00:00")
time_label = tk.Label(root, textvariable=time_var, font=("Arial", 24))
time_label.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack(side=tk.LEFT, padx=5, pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_timer, state=tk.DISABLED)
stop_button.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
