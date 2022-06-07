class TrueString:
    def __init__(self, word1, word2, sum1, sum2):
        self.word1 = word1
        self.word2 = word2
        self.sum1 = sum1
        self.sum2 = sum2

    @property
    def razdel(self):
        self.sum1 = 0
        self.sum2 = 0
        if isinstance(self.word1, list) or isinstance((self.word2), list or set or tuple or int or bool):
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
        else:
            return 'произошла ошибика'


oj1 = 'kdfskjf'
oj2 = 'dsfsдлавввввввввво.'
print(TrueString(oj1, oj2, 0, 0).razdel)
print(TrueString(oj1, oj2, 0, 0).sravnenie)
