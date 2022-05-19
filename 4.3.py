config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config = list(config)
wlist = []

for i in config:
    if i == '1':
        wlist.append(i)
        break

for i in config:
    if i == '3':
        wlist.append(i)
        break

for i in config:
    if i == '1':
        wlist.append(i)
        break

for i in config:
    if i == '0':
        wlist.append(i)
        break

for i in config:
    if i == '2':
        wlist.append(i)
        break

for i in config:
    if i == '0':
        wlist.append(i)
        break

for i in config:
    if i == '3':
        wlist.append(i)
        break

for i in config:
    if i == '0':
        wlist.append(i)
        break

for i in config:
    if i == '1':
        wlist.append(i)
        break

for i in config:
    if i == '0':
        wlist.append(i)
        break

for i in config:
    if i == '0':
        wlist.append(i)
        break

ola = wlist[2] + wlist[3]

wlist.remove(wlist[3])
wlist.remove(wlist[3])
wlist.insert(2, ola)
wlist[3] = '2'

ola2 = wlist[3] + wlist[4]
wlist.remove(wlist[4])
wlist.remove(wlist[3])
wlist.insert(3, ola2)

ola3 = wlist[4] + wlist[5]
wlist.remove(wlist[5])
wlist.remove(wlist[6])
wlist.insert(4, ola3)

wlist[5] = '1'
wlist[6] = '0'

ola4 = wlist[5] + wlist[6] + wlist[7]
wlist.remove(wlist[7])
wlist.remove(wlist[6])
wlist.remove(wlist[5])
wlist.remove(wlist[4])
wlist.insert(5, ola4)
wlist.insert(0, '1')

print(*wlist)
