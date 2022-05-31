def is_prime(number):
    if number < 1001:
        if int(number):
            print('число простое')
            return True

        else:
            return False

    else:
        print('число больше 1000')


is_prime(3.4)
