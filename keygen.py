from math import sin
import sympy as sp


def f(x, y):
    return (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3


def main():
    x, y = input('Введите координаты x1 и y1: ').split(' ')
    x1, x2 = input('Введите координаты x2 и y2').split(' ')

    y_f = f(x, y)
    print(y_f)

    if y_f == 0:
        print(f"Точка ({x}, {y}) находится на графике функции (x^2 + y^2 - 1)^3 - x^2 * y^3 = 0")
    else:
        print(f"Точка ({x}, {y}) не находится на графике функции (x^2 + y^2 - 1)^3 - x^2 * y^3 = 0")


class KeyGen:
    def __init__(self):
        pass


class KeyInput:
    def __init__(self, key):
        self.key = key
        try:
            len(self.key.split('-')) == 4
        except ValueError:
            raise ValueError("Key must be in format XXXX-YYYY-ZZZZ-1234")

    def part1_validate(self, part):
        pass

    def part2_validate(self, part):
        pass

    def part3_validate(self, part):
        pass

    def part4_validate(self, part):
        pass

    def validate(self):
        if [len(x) == 4 for x in self.key.split('-')] and self.key.count('-') == 3:
            part1, part2, part3, part4 = self.key.split('-')
            if all([self.part1_validate(part1), part2_validate(part2),
                    part3_validate(part3), part4_validate(part4)]):
                return True
            else:
                raise ValueError("Key is incorrect")
        else:
            raise ValueError("Key must be in format XXXX-YYYY-ZZZZ-1234")

    def main(self):
        if self.validate():
            print('Successful!')


if __name__ == "__main__":
    main()
