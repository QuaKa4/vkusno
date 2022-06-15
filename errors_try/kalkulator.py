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

    def kalkulator_try_1(self):
        try:
            int(self.number_1) and int(self.number_2)
        except MyError:
            raise MyError('ti ne zaraza')

    def kalkulator_try_2(self):
        try:
            self.oper == '+' or '-' or '*' or '/' or '**' or '//'

        except MyError:
            raise MyError('ti zaraza')

    def kalkulator_deystviya(self):
        self.number_1 = int(self.number_1)
        self.number_2 = int(self.number_2)

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
        else:
            return 'sdfsddf'


hwh = Kallculator()
hwh.kalkulator_try_1()
hwh.kalkulator_try_2()
print(hwh.kalkulator_deystviya())

# '+' or '-' or '*' or '/' or '**' or '//'
