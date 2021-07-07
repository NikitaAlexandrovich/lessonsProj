from math import *


def positive_num(num):
    pass

def task_num_one():
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
        print("Прямоугольный треугольник \n")
    elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (c * c + b * b < a * a):
        print("Тупоугольный треугольник \n")
    else:
        print("Остроугольный треугольник \n")

    print("Площадь: %.2f" % s)

def task_num_two():
    length_rib = abs(float(input("Введите длину ребра основания треугольной пирамиды: ")))
    length_h = abs(float(input("Введите длину высоты для этой пирамиды: ")))
    b = sqrt((length_h ** 2) + (((sqrt(3) / 3) * length_rib) ** 2))
    print(b)
    pyramid_volume = (length_h * pow(length_rib, 2)) / (4 * sqrt(3))
    pyramid_area = ((sqrt(3)/4) * pow(length_rib, 2)) + ((3 / 2) * length_rib * sqrt(((pow(b, 2)) - (pow(length_rib, 2)) / 4)))

    print("Обьем правильной треульной пирамиды: %.2f" % pyramid_volume)
    print("Площадь поверхности правильной пирамиды: %.2f" % pyramid_area)

def task_num_three():
    num = int(input("Введите число: "))
    print(-356 < num <= -1 or 14 < num > 56 or 100 <= num >= 234 or num >= 500)

def task_num_four():
    first, second = float(input("Введите число: \n")), float(input("Введите другое число: \n"))
    desigion = input("Что сделать (+ - * / ^)")

    if desigion == "+":
        print(first + second)
    elif desigion == "-":
        print(first - second)
    elif desigion == "*":
        print(first * second)
    elif desigion == "^":
        print(first, " в степени ", second, " = ", pow(first, second))
    elif desigion == "/":
        print(first / second)
    else:
        print("Таких действий не умеем")

def task_num_five():
    pass

def task_num_six():
    list_num = []

    for num in range(5):
        new_num = int(input("Введите число "))
        list_num.append(new_num)

    list_num.sort(reverse=True)
    print("Максимальное ", list_num[0])
    print("Минимальное ", list_num[4])
    print(list_num[1],list_num[2],list_num[3])

def task_num_seven():
    """

    мне тут лень делать
    но короче находим длину числа и возводим 10 в степень на половину менишь
    для деления пополам и потом внутри числа тоже деоим по уменьшающейся сттепени десятки

    :return:
    """
    pass

def task_num_eight():
    pass


if __name__ == '__main__':
    # task_num_one()
    # task_num_two()
    # task_num_three()
    # task_num_four()
    # task_num_five()
    # task_num_six()
    task_num_seven()
    # task_num_eight()