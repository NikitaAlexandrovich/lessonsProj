if __name__ == '__main__':
    num = int(input("Введите трехзначное число: "))

    first = num % 10
    num = num // 10
    second = num % 10
    num = num // 10

    print("Сумма цифр трехзначного числа равна: ", first + second + num)