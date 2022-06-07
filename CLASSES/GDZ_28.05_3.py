class KgToPounds:

    def __init__(self, kg):
        self._kg = kg

    def to_pounds(self):
        return self._kg * 2.205

    @property
    def unit(self):
        return self._kg

    @unit.setter
    def unit(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


kg_to_pounds = KgToPounds(834)
oj = kg_to_pounds.unit = 4.4
print(oj)
