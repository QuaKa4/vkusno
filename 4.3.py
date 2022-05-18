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
wlist.remove(wlist[4])
wlist.insert(2, ola)

print(wlist)
