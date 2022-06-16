from tkinter import *

window = Tk()
window.title("u gay")
window.geometry('200x100')


class Cls():
    @staticmethod
    def cl_1():
        nnn.insert(9999, '1')

    @staticmethod
    def cl_2():
        nnn.insert(9999, '2')

    @staticmethod
    def cl_3():
        nnn.insert(9999, '3')

    @staticmethod
    def cl_4():
        nnn.insert(9999, '4')

    @staticmethod
    def cl_5():
        nnn.insert(9999, '5')

    @staticmethod
    def cl_6():
        nnn.insert(9999, '6')

    @staticmethod
    def cl_7():
        nnn.insert(9999, '7')

    @staticmethod
    def cl_8():
        nnn.insert(9999, '8')

    @staticmethod
    def cl_9():
        nnn.insert(9999, '9')

    @staticmethod
    def cl_0():
        nnn.insert(9999, '0')

    @staticmethod
    def cl_m():
        nnn.insert(9999, '-')

    @staticmethod
    def cl_p():
        nnn.insert(9999, '+')

    @staticmethod
    def cl_f():
        nnn.insert(9999, '*')

    @staticmethod
    def cl_d():
        nnn.insert(9999, '/')

    @staticmethod
    def cl_del():
        nnn.delete(first=0, last=9999)


global Entry

nnn = Entry(width=20)
nnn.grid(column=4, row=1)

nnn_get = nnn.get()

allowed_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/']

nnn_zametki = Entry()
nnn_zametki.grid(column=4, row=3)

lbl = Label(text='заметки')
lbl.grid(column=4, row=2)

button_1 = Button(window, text="1", command=Cls.cl_1)
button_1.grid(column=0, row=1)
button_2 = Button(window, text="2", command=Cls.cl_2)
button_2.grid(column=1, row=1)
button_3 = Button(window, text="3", command=Cls.cl_3)
button_3.grid(column=2, row=1)
button_4 = Button(window, text="4", command=Cls.cl_4)
button_4.grid(column=0, row=2)
button_5 = Button(window, text="5", command=Cls.cl_5)
button_5.grid(column=1, row=2)
button_6 = Button(window, text="6", command=Cls.cl_6)
button_6.grid(column=2, row=2)
button_7 = Button(window, text="7", command=Cls.cl_7)
button_7.grid(column=0, row=3)
button_8 = Button(window, text="8", command=Cls.cl_8)
button_8.grid(column=1, row=3)
button_9 = Button(window, text="9", command=Cls.cl_9)
button_9.grid(column=2, row=3)
button_0 = Button(window, text="0", command=Cls.cl_0)
button_0.grid(column=1, row=4)

button_p = Button(window, text="+", command=Cls.cl_p)
button_p.grid(column=3, row=2)
button_m = Button(window, text="-", command=Cls.cl_m)
button_m.grid(column=3, row=1)
button_f = Button(window, text="*", command=Cls.cl_f)
button_f.grid(column=3, row=3)
button_d = Button(window, text="/", command=Cls.cl_d)
button_d.grid(column=3, row=4)
button_r = Button(window, text="=")
button_r.grid(column=2, row=4)
button_del = Button(window, text="C", command=Cls.cl_del)
button_del.grid(column=0, row=4)


def oj_1():
    if nnn:
        button_r.pack()
        button_d.pack()
        button_f.pack()
        button_p.pack()


window.mainloop()
