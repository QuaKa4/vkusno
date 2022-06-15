class TrueString:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.sum1 = 0
        self.sum2 = 0

    @property
    def razdel(self):
        _sum = 0
        if not isinstance(self.word1, str) and isinstance(self.word2, str):
            print('вводить можно только строковые значения')
        else:
            list1 = list(self.word1)
            list2 = list(self.word2)
            for el1 in list1:
                pon1 = ord(el1)
                self.sum1 = pon1 + self.sum1

            for el2 in list2:
                pon2 = ord(el2)
                self.sum2 = pon2 + self.sum2
            return self.sum1, self.sum2

    @property
    def sravnenie(self):
        if isinstance(self.sum1, int) and isinstance(self.sum2, int):
            if self.word1 > self.word2:
                return 'первая строка имеет значение больше'
            elif self.word2 > self.word1:
                return 'вторая строка имеет значение больше'
            elif self.word2 == self.word1:
                return 'значения равны'


oj1 = 'dsfsдлавввввввввво'
oj2 = 'dsfsдлавввввввввво'
print(TrueString(oj1, oj2).razdel)
print(TrueString(oj1, oj2).sravnenie)
