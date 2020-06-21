from tkinter import *

def handler(event):
    print('Hello hui!')

def handler2(event):
    exit()

root = Tk()#переменная связываемая с объектом

e = Entry(root, width=20)
b = Button(root, text='Преобразователь1')
l = Label(root, bg='black', fg='white', width=20
b.bind('Button-1', handler)        
b.pack()



root.mainloop()
