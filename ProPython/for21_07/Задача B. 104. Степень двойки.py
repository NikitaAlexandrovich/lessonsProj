n = int(input())
rez = ['NO','YES']
if n <= 0:
    print("NO")
else:
    print(rez[n & (n - 1) == 0])
