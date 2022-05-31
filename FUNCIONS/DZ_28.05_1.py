def arethmetic(num1, num2, operation):
    if operation == '*':
        print(num1 * num2)

    elif operation == '-':
        print(num1 - num2)

    elif operation == '+':
        print(num1 + num2)

    elif operation == '/':
        print(num1 / num2)

    else:
        print("операция не распознана")


arethmetic(2, 2, '*')


def kurva(numb1, numb2, op):
    for element in op:
        if element == "+":
            print(numb1 + numb2)

        elif element == "/":
            print(numb1 / numb2)

        elif element == "*":
            print(numb1 * numb2)

        elif element == "-":
            print(numb1 - numb2)

        else:
            print("неопознанная операция")


kurva(4, 4, ["+", "-", "tdeg"])
