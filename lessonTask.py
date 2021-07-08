from datetime import timedelta
from math import pow, sqrt, factorial


if __name__ == '__main__':
    while True:
        try:
            decision = int(input("В задании было 18 задач... Напишите номер какой Вы бы запустили. Другое число завершит это всё :) "))
            if decision == 1:
                # first
                print(1 << 179)
                print(pow(2, 179))
                print(2 ** 179)

            elif decision == 2:
                # second
                side_one = 179
                side_two = 971
                print(sqrt((side_one ** 2) + (side_two ** 2)))

            elif decision == 3:
                # third
                side_one = int(input("Одна сторона: "))
                side_two = int(input("Другая сторона: "))
                print(sqrt((side_one ** 2) + (side_two ** 2)))

            elif decision == 4:
                # fours
                print("Длины сторон треугольника:")
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                if a + b > c and a + c > b and b + c > a:
                    print("YES")
                else:
                    print("NO")

            elif decision == 5:
                # five
                num = pow(179, 10)
                print(pow(num, 2))

            elif decision == 6:
                # six
                number = int(input("Введите число для факториала: "))
                sum_num = 0
                for itera in range(number + 1):
                    sum_num = sum_num + itera ** 2
                print(sum_num)

            elif decision == 7:
                # seven
                k = int(input("Введите k для задачи 7: "))
                n = int(input("Введите n для задачи 7: "))

                result = (factorial(n)) / ((factorial(k)) * (factorial(n - k)))

                print(result)

            elif decision == 8:
                # eight
                """
                сделаем условие что penguin нельзя изменять никак
                и пенгвин является массивом
                """
                penguin = ["   _~_    ",
                           "  (o o)   ",
                           " /  V  \ ",
                           "/(  _  )\ ",
                           "  ^^ ^^   "]
                free_str = [" ",
                            " ",
                            " ",
                            " ",
                            " "]
                num = int(input("Введите количесво пингвинов (от 1 до 9): "))
                if 1 <= num <= 9:
                    for itera in range(num):
                        for a in range(len(penguin)):
                            print(penguin[a] + free_str[a])
                            # странно то что мы можем установить end= для корректного вывода пингвина получится что он будет идти один за одним в солбец а не в строку как хотелось бы(
                else:
                    print("Грустно(((, надо было от 1 до 9")

            elif decision == 9:
                # nine
                n = float(input("Введите число n для задачи 9 (подсчет  n + nn + nnn) "))
                print(n + n ** 2 + n ** 3, "Исрользование **")
                print(n + pow(n, 2) + pow(n, 3), "Использование pow")

            elif decision == 10:
                # ten
                second = int(input("Введите секунды для их перевода: "))
                print(str(timedelta(seconds=second)))

            elif decision == 11:
                # eleven
                print(factorial(20))

            elif decision == 12:
                # twelve
                first = int(input("Введите первое число: "))
                second = int(input("Введите второе число: "))
                if first > second:
                    print(f"Наибольшее {first}")
                else:
                    print(f"Наибольшее {second}")

            elif decision == 13:
                # thirteen
                first = int(input("Введите первое число: "))
                second = int(input("Введите второе число: "))
                if first > second:
                    print(1)
                elif first == second:
                    print(0)
                else:
                    print(2)

            elif decision == 14:
                # fourteen
                num = int('179' * 50)
                print(num ** 2)

            elif decision == 15:
                # fifteen
                year = int(input("Введите год для проверки:"))
                if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                    print("Високосный год ", year)
                else:
                    print("НЕ високосный год ", year)

            elif decision == 16:
                # sixteen
                year = int(input("Введите год для проверки:"))
                if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                    print("Високосный год ", year)
                else:
                    print("НЕ високосный год ", year)

            elif decision == 17:
                # seventeen
                x_first = int(input("Введите первую координату Х"))
                y_first = int(input("Введите первую координату У"))
                x_second = int(input("Введите вторую координату Х"))
                y_second = int(input("Введите вторую координату У"))
                dx = abs(x_first - x_second)
                dy = abs(y_first - y_second)
                if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                    print("Сможет!")
                else:
                    print("Не сможет(")

            elif decision == 18:
                # eighteen
                print('A' * 100)

            else:
                print("Завершили программу!")
                break
        except Exception as ex:
            print("Очень грустно что ввели ерунду( Попробуйте заново и у Вас получится!")
