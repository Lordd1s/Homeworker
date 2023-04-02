import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)

        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display = tk.Label(
            self.master,
            textvariable=self.display_var,
            font=("Arial", 24),
            width=18,
            height=2,
            anchor="e",
            bg="white",
            bd=5,
            relief="raised",
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.button_values = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "C", "/",
            "="
        ]
        self.buttons = []
        for i, value in enumerate(self.button_values):
            row = i // 4 + 1
            col = i % 4
            button = tk.Button(
                self.master,
                text=value,
                font=("Arial", 18),
                width=4,
                height=2,
                command=lambda v=value: self.on_button_click(v),
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

    def on_button_click(self, value):
        if value == "C":
            self.display_var.set("0")
        elif value == "=":
            try:
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except (SyntaxError, ZeroDivisionError):
                self.display_var.set("ERROR")
        else:
            current = self.display_var.get()
            if current == "0" and value != ".":
                current = ""
            self.display_var.set(current + value)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
