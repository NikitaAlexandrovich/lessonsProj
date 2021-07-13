str = [int(i) for i in input().split()]
sum_num = 0
len_str = len(str) - 1
for i in range(0,len_str + 1):
    sum_num = sum_num + sum_num[i]
print(sum_num)