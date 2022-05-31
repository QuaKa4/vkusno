per = lambda y: y + 1

i = 0


def ok():
    global i
    i += 1
    return i


print(per(i))
