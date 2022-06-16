class MyError(Exception):
    pass


class CalculatorFunctional:
    def __init__(self):
        number_1 = input('введите число:')
        number_2 = input('введите второе число:')
        oper = input('ведите операцию:')
        self.oper = oper
        self.number_1 = number_1
        self.number_2 = number_2
        try:
            self.number_1 = float(self.number_1)
            self.number_2 = float(self.number_2)
        except MyError:
            raise MyError(f'Value error {self.number_1} or {self.number_2}')

    def check_operation_fill(self):
        operation = ['+', '-', '*', '/']

        for element in operation:
            check_oper = self.oper == element
        if check_oper == None:
            raise MyError('operation unknown')
        if self.oper == '+':
            ret_1 = self.number_1 + self.number_2
            return ret_1
        elif self.oper == '-':
            return self.number_1 - self.number_2
        elif self.oper == '*':
            return self.number_1 * self.number_2
        elif self.oper == '/':
            return self.number_1 / self.number_2


calculator_func = CalculatorFunctional()
print(calculator_func.check_operation_fill())

# '+' or '-' or '*' or '/' or '**' or '//'
