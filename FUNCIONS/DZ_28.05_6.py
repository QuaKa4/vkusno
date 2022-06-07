def is_prime(number):
    if number <= 1000 and number >= 1:
        if number % 2 == 0:
            return 'число простое'
        else:
            return "число составное"
    else:
        return "число больше 1000 или меньше 1"


print(is_prime(6))
