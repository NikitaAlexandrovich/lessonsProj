import math

number = int(input())
str_jcp = input()

for itr in '+-*/=':
    str_jcp = str_jcp.replace(itr, ' ' + itr + ' ')
str_jcp = str_jcp.split()
str_jcp = [z if z in '+-*/=' else int(z) for z in str_jcp]

while True:
    try:
        slash_index = str_jcp.index('/')
    except Exception as ex:
        break
    str_jcp[slash_index] = '*'


    def search(x, num):
        if math.gcd(x, num) != 1:
            return "Error"
        first, second, third = 1, 0, x
        first_v, second_v, third_v = 0, 1, num

        while third_v != 0:
            q = third // third_v
            first_v, second_v, third_v, first, second, third = (first - q * first_v), (second - q * second_v), (
                        third - q * third_v), first_v, second_v, third_v
        return first % num

    str_jcp[slash_index + 1] = search(str_jcp[slash_index + 1], number)

if "Error" in str_jcp:
    print("@")
else:
    while True:
        try:
            slash_index = str_jcp.index('*')
        except Exception as ex:
            break
        str_jcp[slash_index - 1] = (int(str_jcp[slash_index - 1]) * int(str_jcp[slash_index + 1])) % number
        del str_jcp[slash_index + 1]
        del str_jcp[slash_index]

    while True:
        try:
            slash_index = str_jcp.index('+')
        except:
            break
        str_jcp[slash_index - 1] = (int(str_jcp[slash_index - 1]) + int(str_jcp[slash_index + 1])) % number
        del str_jcp[slash_index + 1]
        del str_jcp[slash_index]

    print(str_jcp[0])