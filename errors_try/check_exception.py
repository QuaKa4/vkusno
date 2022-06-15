class AnyException(Exception):
    pass


class CheckException:
    @staticmethod
    def _check_exception(side_1):
        side_2 = 0
        sum_sides = side_2 + side_1
        return sum_sides

    def prizma(self, side):
        try:
            self._check_exception(side)
        except TypeError:
            raise TypeError('side_1 or side_2 is not equol')

    def prizma_two(self, side):
        try:
            self._check_exception(side)
        except TypeError:
            raise TypeError('side_1 or side_2 is not equol')


check_exception = CheckException()
check_exception.prizma('hjhjhj')
