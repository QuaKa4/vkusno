list_data = ['12', 12, '98', '634', 'jdfs']
for element in list_data:
    print(f'{element} kgkgkg')


def all_data(data1, data2):
    sum_data = int(data1) + data2
    print(sum_data)


all_data(int(list_data[0]), list_data[1])

x = lambda a: a + int(list_data[0])
print(x(5))
