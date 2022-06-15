from tkinter import *


class MyError(Exception):
    pass


class Kallculator:
    def __init__(self):
        number_1 = input('введите число:')
        number_2 = input('введите второе число:')
        oper = input('ведите операцию:')
        self.oper = oper
        self.number_1 = number_1
        self.number_2 = number_2
        self.number_1 = int(self.number_1)
        self.number_2 = int(self.number_2)

    def kalkulator_try_1(self):
        try:
            int(self.number_1) and int(self.number_2)
        except Exception:
            raise Exception('ti ne zaraza')

    def kalkulator_try_2(self):
        try:
            if self.oper == '+' or '-' or '*' or '/' or '**' or '//':
                raise MyError('ti zaraza')
        except MyError:
            raise MyError('ti zaraza')

    def kalkulator_deystviya(self):
        if self.oper == '+':
            return self.number_1 + self.number_2
        elif self.oper == '-':
            return self.number_1 - self.number_2
        elif self.oper == '*':
            return self.number_1 * self.number_2
        elif self.oper == '/':
            return self.number_1 / self.number_2
        elif self.oper == '**':
            return self.number_1 ** self.number_2
        elif self.oper == '//':
            return self.number_1 // self.number_2


hwh = Kallculator()
hwh.kalkulator_try_2()
hwh.kalkulator_try_1()
print(hwh.kalkulator_deystviya())

# '+' or '-' or '*' or '/' or '**' or '//'


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.mainloop()
