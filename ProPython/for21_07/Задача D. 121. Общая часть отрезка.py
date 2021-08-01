N = int(input())
l, r = input().split()
l = int(l)
r = int(r)
for i in range(N - 1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > l: l = a
    if b < r: r = b

if l >= r:
    print(0)
else:
    print(r - l)