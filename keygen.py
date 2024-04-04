from math import sin


def f(x, y):
    return (x**2 + y**2 - 1)**3 - x**2 * y**3


def main():
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))

    y_f = f(x, y)
    print(y_f)

    if y_f == 0:
        print("Точка ({}, {}) находится на графике функции y = |x| + sin(x)".format(x, y))
    else:
        print("Точка ({}, {}) не находится на графике функции y = |x| + sin(x)".format(x, y))


if __name__ == "__main__":
    main()
