# Задание1
my_dict = {'a': 500,
           'b': 5874,
           'c': 560,
           'd': 400,
           'e': 5824,
           'f': 20}
keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(keys)

# Задание2
rows = int(input("Введите до какой строки выводить треугольник"))
row = [1]
for i in range(rows):
    print(row)
    row = [sum(x) for x in zip([0] + row, row + [0])]

# Задание3
listr = input("Введите числа для внесения в список и кортеж через запятую: ").split(",")
for i in range(len(listr)):
    listr[i] = int(listr[i])
print(listr)
tuplic = tuple(x for x in listr)
print(tuplic)

# Задание4
listf = input("Введите элементы первого списка через пробел: ").split(" ")
lists = input("Введите элементы второго списка через пробел: ").split(" ")
result = list(filter(lambda el: el not in lists, listf))
print(result)

# ЛИБО

nwRes = [el for el in listf if el not in lists]
print(nwRes)

# Задание5
strOld = input("Введите строку: ")
oldW = input("Введите заменяемую подстроку: ")
newW = input('Введите новую подстроку: ')
strIn = strOld.find(oldW)
while i != -1:
    lenStr = len(oldW)
    strOld = strOld[0:i] + newW + strOld[i + 1:]
    i = strOld.find(oldW)

print(strOld)

# Задание6
import numpy as np
x = int(input("Введите размерность матрицы: "))
array_rand_val = np.random.random((x, x))
print(array_rand_val)
b = np.rot90(array_rand_val)
print("Сумма главной диагонали: ", sum(np.diagonal(array_rand_val)))
print("Сумма побочной диагонали: ", sum(np.diagonal(b)))


# Задание7
# ну короче регулярные выражения юзаем
import re
st = re.sub(r'[^\w\s]',' ',input("Введите текст: ")).split()
print(st)

# Задание8
import random
array = []
for i in range(20):
    array.append(int(random.random() * 20) - 10)
positive = []
negative = []
for i in array:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
print(positive, " ", negative)


# Задание9
# нет идеи как решить

# Задание10
# картинка не прогружена из юпитера(
# Задание11
# картинка не прогружена из юпитера(
