def is_year_leap(year: int = 365):
    if year == 365:
        return True
    else:
        return False


print(is_year_leap(365))


def isyear(year: bool = True):
    if year == True:
        print(365)
    else:
        print('lol')


isyear()


class Valera():
    def __init__(self, pron):
        self.pron = pron

    def ne_valera(self):
        print(self.pron)
        self._oracle()

    @staticmethod
    def _oracle():
        print('ch')


dogp = Valera(6)
dogp.ne_valera()
