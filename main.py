*list_data, = '12', '12', '98', '634', 'jdfs'
print(f'gof{list_data}fff')
print(*list_data)

bullet = ['2', '1', '98', '6', '09']
print(f'gof{bullet}fff')
print(*bullet)


def names_dict(**kwargs):
    name_dict = kwargs
    print(name_dict)
    one_data = name_dict.get('Leo')
    print(one_data)


names_dict(Leo='Ok', Ivan='done', Vasili='okok')


def foo(*args):
    name = args
    for n in name:
        ok = f'Hi people {n}'
        print(ok)


foo(['oooo', 'aaaa'], '2211', '9090')


def no_args(list, number, number2):
    name = list, number, number2
    for n in name:
        okk = f'Hi people {n}'
        print(okk)


no_args(['oooo', 'aaaa'], '2211', '9090')

num1_dict = {'a': 'b', 'c': 'd'}
one_data = num1_dict.get('a')

num2_dict = {'s': 'q'}
two_data = num2_dict.get('s')

common_data = str(one_data) + ' ' + str(two_data)
print(common_data)

f_select = f'{one_data} {two_data}'
print(f_select)

# Unification the dicts
common_dict = {**num1_dict, **num2_dict}
print(common_dict)

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
