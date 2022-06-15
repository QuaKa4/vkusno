class AnyErrorException(Exception):
    pass


def valerchik(wish_list):
    try:
        sum_el = 0
        for element in wish_list:
            sum_el = sum_el + element
        oj = len(wish_list)
        qvq = sum_el / oj
        return qvq
    except TypeError:
        raise AnyErrorException('return error')


print(valerchik([3, 2, 22, 1234, 234234, 22]))
