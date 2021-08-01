if __name__ == '__main__':
    year = int(input("Введите год для проверки:"))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Високосный год ", year)
    else:
        print("НЕ високосный год ", year)