import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("450x200")
frm = ttk.Frame(root, padding=20)
root.resizable(width=False, height=False)
frm.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

ttk.Label(frm, text="Введите первое число: ").grid(column=0, row=0)
num1 = ttk.Entry(frm)
num1.grid(column=1, row=0)

ttk.Label(frm, text="Введите второе число: ").grid(column=0, row=1)
num2 = ttk.Entry(frm)
num2.grid(column=1, row=1)


def get_sum():
    nums1 = int(num1.get())
    nums2 = int(num2.get())
    val = int((nums2 * (nums2 + 1)) / 2 - ((nums1 - 1) * ((nums1 - 1) + 1)) / 2)
    print(f"Результат: {val}")


ttk.Button(frm, text="Результат", command=get_sum).grid(column=1, row=3)

root.mainloop()
