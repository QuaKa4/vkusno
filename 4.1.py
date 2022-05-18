nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = list(nat)

nat[42] = 'b i'
nat[40] = 'G i g'

print(" ".join(nat))
