from tkinter import *

root = Tk(className='나의 실행창이지요')
root.geometry('500x500')


b1 = Button(root, text='테스트')
b1.grid(row=0, column=0, padx=215, pady=200) 

def btn_click(event):
    print("버튼이 클릭되었습니다")

b1.bind('<Button-1>', btn_click)

root.mainloop()

#pyinstaller --onefile your_script_name.py
