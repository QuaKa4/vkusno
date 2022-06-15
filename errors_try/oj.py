from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("дрочильня")
window.geometry('400x250')

button_1 = Button(window, text="принять", background='black', foreground='white')
button_1.grid(column=1, row=0)

combox_1 = Combobox(window, background='black', foreground='white')
combox_1['values'] = 1, 2, 3, 4, 5, 6, 7
combox_1.current(0)
combox_1.grid(column=0, row=0)

window.mainloop()
