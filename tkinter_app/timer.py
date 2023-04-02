import tkinter as tk


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")
        self.master.resizable(False, False)

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.time_label = tk.Label(
            self.master,
            textvariable=self.time_var,
            font=("Arial", 24),
            width=10,
            height=2,
            anchor="center",
            bg="white",
            bd=5,
            relief="raised",
        )
        self.time_label.pack(padx=10, pady=10)

        self.start_button = tk.Button(
            self.master,
            text="Start",
            font=("Arial", 18),
            width=8,
            height=2,
            command=self.start_timer,
        )
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(
            self.master,
            text="Stop",
            font=("Arial", 18),
            width=8,
            height=2,
            command=self.stop_timer,
            state="disabled",
        )
        self.stop_button.pack(side="right", padx=10, pady=10)

        self.elapsed_time = 0
        self.timer_running = False

    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def update_timer(self):
        if self.timer_running:
            self.elapsed_time += 1
            hours = self.elapsed_time // 3600
            minutes = (self.elapsed_time % 3600) // 60
            seconds = self.elapsed_time % 60
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_var.set(time_string)
            self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = Timer(root)
    root.mainloop()

