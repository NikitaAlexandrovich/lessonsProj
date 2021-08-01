a, b = input().split()
a = int(a)
b = int(b)
res = ''
array = [i + 1 for i in range(a)]
array = array[-b:] + array[:-b]
for i in range(a):
    if i < a - 1:
        res = res + str(array[i]) + " "
    else:
        res = res + str(array[i])

print(res)
        # print(array[i])



        # print(array[i], end=" ")