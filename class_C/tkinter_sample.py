import tkinter as tk

root = tk.Tk()

# Label
widget1 = tk.Label(root, text="이것은 Label입니다.")
widget1.pack()

# Button
widget2 = tk.Button(root, text="이것은 Button입니다.")
widget2.pack()

# Text
widget3 = tk.Text(root)
widget3.pack()

# Listbox
widget4 = tk.Listbox(root)
widget4.pack()

root.mainloop()
