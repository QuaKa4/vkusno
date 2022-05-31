def season(mounth):
    if mounth >= 3 and mounth <= 5:
        print('spring')

    elif mounth >= 6 and mounth <= 8:
        print('summer')

    elif mounth >= 9 and mounth <= 11:
        print('autamn')

    elif mounth == 12 or mounth <= 2:
        print('winter')

    else:
        print('такого месяца нет')


season(2)
