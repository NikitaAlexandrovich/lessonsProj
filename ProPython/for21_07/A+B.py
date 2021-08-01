a, b = input().split()
if "." in a or "." in b:
    a = float(a)
    b = float(b)
else:
    b = int(b)
    a = int(a)
print(a + b)


