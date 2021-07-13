str = [int(i) for i in input("Введите числа: ").split()]
temp = []

str.sort()
len_str = len(str) - 1
perem = 100000

if len(str) != 1:
    for i in range(len(str) - 1):
        if str[i] == str[i + 1] and str[i] != perem:
            temp.append(str[i])
            perem = str[i]
    for j in range(len(str)):
        if str[-1] == str[-2] and str[j] != perem:
            temp.append(str[j])

for r in range(len(temp)):
    print(temp[r])

"""
Введите числа: 1 2 3 4 5 6 7 8 9 10 1 5
1
5

"""
