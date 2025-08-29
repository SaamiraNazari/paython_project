#
# from tkinter import *
#
# window= Tk()
# # اندازه پنجره باز شده
# window.geometry("800x800")
# window.minsize(300,300)
# #نام پنجره
# window.title("Instahhed Downloader")
# #مقداری که به صورت لیبل در پنجره چاپ می شود
# label= Label(window, text="Hello Samira")
# label.pack()
# #تعریف دکمه ها
# def hello():
#    label.config(text=input.get())
#
# button = Button(window, text="Click Me", command=hello,bg="red")
# button.pack()
#
# input=Entry(window)
# input.pack()
#
# # button.place(x=50,y=50)
# #lable option in tkinter
# window.mainloop()
# # label= Label(window,text="please enter the tow number",bg="red",fg="white")
# # label.pack()
# # def hello():
# #     print("hello")
# #
# # input=Entry(window)
# # input.pack()
# # window.mainloop()

import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception:
            screen.set("خطا")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# ساخت پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب ساده")
root.geometry("300x400")

# نمایشگر
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", justify="right")
entry.pack(fill="both", ipadx=8, pady=10)

# دکمه‌ها
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", width=5, height=2)
        b.pack(side="left", padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()