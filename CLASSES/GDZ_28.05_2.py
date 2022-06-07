class TriangleChecker:
    @staticmethod
    def is_trangle(sides):
        if isinstance(sides, str):
            return 'Нужно вводить только числа!'
        else:
            if len(sides) >= 4 or len(sides) < 3:
                return 'треугольник включает только три стороны'
            else:
                if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
                    return 'С отрицательными числами или нулями ничего не выйдет!'
                else:
                    if sides[1] > sides[2] + sides[0]:
                        return 'Жаль, но из этого треугольник не сделать'
                    elif sides[2] > sides[0] + sides[1]:
                        return 'Жаль, но из этого треугольник не сделать'
                    elif sides[0] > sides[1] + sides[2]:
                        return 'Жаль, но из этого треугольник не сделать'

                    else:
                        return f'Ура, можно построить треугольник! Tреугольник получился {sides[0]} на {sides[1]} на {sides[2]}'


print(TriangleChecker.is_trangle([3, 2, 1]))
