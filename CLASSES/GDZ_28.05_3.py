# class KgToPounds:
#     def __init__(self, kg):
#         self.ne_kg = kg
#
#     def to_pounds(self):
#         return self.ne_kg * 2.205
#
#     def set_kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.ne_kg = new_kg
#         else:
#             raise ValueError('Килограммы задаются только числами')
#
#     def get_kg(self):
#         return self.ne_kg
#
#     oj = property(get_kg, set_kg)
#
#     jjj = to_pounds(5) and set_kg(4)
#
#     print(jjj)
class KgToKilo:
    def __init__(self, kg):
        self.ne_kg = kg

    def to_gramms(self):
        return self.ne_kg * 10

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.ne_kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def get_kg(self):
        return self.ne_kg

    kg = property(get_kg, set_kg)


oj = KgToKilo(912)
print(oj.to_gramms())
print(oj.get_kg())
oj.set_kg(5)
print(oj.get_kg())
