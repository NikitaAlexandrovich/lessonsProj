from math import *


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
        if first == 0 or second == 0:
            print("Вы чтооо делить на ноль????")
        else:
            print(first / second)
    else:
        print("Таких действий не умеем")

def task_num_five():
    numbers_of_figure = int(input("Введите число углов (3 для прямоульного треугольника и 4 для квадрата или прямоугольника)"))
    if numbers_of_figure == 4:
        side_one = float(input("Введите первую сторону квадрата или прямоугольника "))
        side_two = float(input("Введите вторую сторону квадрата или прямоугольника "))
        print(f"Площадь квадрата/прямоугольника {side_one * side_two}")
    elif numbers_of_figure == 3:
        side_one = float(input("Введите первый катет "))
        side_two = float(input("Введите второй катет "))
        print(f"Площадь прямоугольного треугольника {0.5 * side_one * side_two}")
    else:
        print("Что-то непонятная фигура, умею прямоугольный треуг и квадрат с прямоугольником")

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
    number = int(input("Введите число для проверки: "))
    nums_list = []
    count = 0

    while number > 0:
        digit = number % 10
        nums_list.append(digit)
        count = count + 1
        number = number // 10

    if count % 2 == 0:
        f_sum = 0
        s_sum = 0
        stop_num = count // 2
        for in_list in range(count):
            if in_list < stop_num:
               f_sum = f_sum + nums_list[in_list]
            elif in_list >= stop_num:
                s_sum = s_sum + nums_list[in_list]

        print(f"Первая часть {s_sum}")
        print(f"Вторая часть {f_sum}")
        if s_sum == f_sum:
            print(True)
        else:print(False)
    else:
        print("Число не симметричное!")

def task_num_eight():
    value_num = int(input("Введите число для отпределения окончания слова: "))

    prog_one = " программистов"
    prog_two = " программист"
    prog_three = " программиста"

    disabled_one = " инвалидов"
    disabled_two = " инвалид"
    disabled_three = " инвалида"


    if value_num >= 0:
        if value_num == 0:
            print(str(value_num) + prog_one)
            print(str(value_num) + disabled_one)
        elif value_num % 100 >= 10 and value_num % 100 <= 20:
            print(str(value_num) + prog_one)
            print(str(value_num) + disabled_one)
        elif value_num % 10 == 1:
            print(str(value_num) + prog_two)
            print(str(value_num) + disabled_two)
        elif value_num % 10 >= 2 and value_num % 10 <= 4:
            print(str(value_num) + prog_three)
            print(str(value_num) + disabled_three)
        else:
            print(str(value_num) + prog_one)
            print(str(value_num) + disabled_one)


if __name__ == '__main__':
    while True:
        try:
            decision = int(input("В домашке было 8 задач... Напишите номер какой Вы бы запустили. Другое число завершит это всё :) "))
            if decision == 1:
                task_num_one()
            elif decision == 2:
                task_num_two()
            elif decision == 3:
                task_num_three()
            elif decision == 4:
                task_num_four()
            elif decision == 5:
                task_num_five()
            elif decision == 6:
                task_num_six()
            elif decision == 7:
                task_num_seven()
            elif decision == 8:
                task_num_eight()
            else:
		print("Завершили программу!")
                break
        except Exception as ex:
            print("Очень грустно что ввели ерунду( Попробуйте заново и у Вас получится!")