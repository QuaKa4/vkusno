class ListNoDuplicate:
    def write_in_list(self, command1, command2):
        shkval = []
        command_ne_1 = list(command1)
        command_ne_2 = list(command2)
        command_ne_1.insert(30, ',')
        command_ne_2.insert(30, ',')

        pron1 = ("".join(command_ne_1))
        pron2 = ("".join(command_ne_2))

        com1 = [int(com1) for com1 in pron1.split(',') if com1.isdigit()]
        com2 = [int(com2) for com2 in pron2.split(',') if com2.isdigit()]

        shkval.append(list(com1) + list(com2))
        one_list = shkval.pop(0)
        del one_list[0:5]
        del one_list[3]
