nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
list_nat = list(nat)

list_nat[40] = 'Gig'
list_nat[42] = 'bi'

print("".join(list_nat))
