def square(side_size):
    a = f"периметр квадрата: {side_size * 4}"
    b = f"длина диагонали квадрата равна: {side_size * 2 ** 0.5}"
    c = f"площадь квадрата равна: {side_size * side_size}"

    adv = a, b, c

    kort = tuple(list(adv))
    print(kort)


square(8)
