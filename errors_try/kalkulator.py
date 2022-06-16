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

    def kalkulator_try(self):
        try:
            self.number_1 = int(self.number_1)
            self.number_2 = int(self.number_2)
        except ValueError:
            raise ValueError('ti zaraza')

        try:
            if self.oper != '+' or '-' or '*' or '/':
                raise MyError('ti zaraza')
        except ValueError:
            if self.oper == '+':
                return self.number_1 + self.number_2
            elif self.oper == '-':
                return self.number_1 - self.number_2
            elif self.oper == '*':
                return self.number_1 * self.number_2
            elif self.oper == '/':
                return self.number_1 / self.number_2


hwh = Kallculator()
print(hwh.kalkulator_try())

# '+' or '-' or '*' or '/' or '**' or '//'
