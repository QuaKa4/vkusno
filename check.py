from check_duplicate import ListNoDuplicate
from enum_lesson import CarsNaming


def lesson_4_5():
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"
    get_class = ListNoDuplicate()
    get_class.write_in_list(command1, command2)


lesson_4_5()


def check_enum():
    com1 = f'lowly {CarsNaming.car1}'
    com2 = f'incredible {CarsNaming.car2}'
    com3 = f'lowly {CarsNaming.car3}'
    com4 = f'lowly {CarsNaming.car4}'
    print(com1, com2, com3, com4)


check_enum()


def stats(data):
    """данные должны быть списком"""
    _sum = sum(data)  # обратите внимание на подчеркивание, чтобы избежать переименования встроенной функции sum
    mean = _sum / float(
        len(data))  # обратите внимание на использование функции float, чтобы избежать деления на целое число
    variance = sum([(x - mean) ** 2 / len(data) for x in data])
    return mean, variance  # возвращаем x,y — кортеж!


m, v = stats([1, 2, 1])

i = 0


def increment():
    global i
    i += 1
