import tkinter as tk
root = tk.Tk()
root.title("Demo Display")
root.geometry("250x250")

x = tk.StringVar()
x.set("Hello")

label = tk.Label(root ,textvariable = x,) 
label.pack()

root.mainloop()
