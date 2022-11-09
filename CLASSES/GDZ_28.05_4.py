class Nicola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def is_ne_nicoli_v_nicolu(self):
        way_1 = 'имя нужно писать буквами, а возраст числами'
        way_3 = f'я {self.name}, мне {self.age} лет'
        if isinstance(self.name, str) and isinstance(self.age, int):
            if self.name != 'Николай':
                return way_2
            else:
                return way_3
        else:
            return way_1


propro = Nicola('Николай', 89).is_ne_nicoli_v_nicolu
print(propro)
