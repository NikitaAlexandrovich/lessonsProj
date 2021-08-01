def toBASEint(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base]
    while n >= base:
        n = n // base
        b += alpha[n % base]
    return ('' if num >= 0 else '-') + b[::-1]


Basein = int(input())
Baseout = int(input())
Number = input()

alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if '.' in Number:
    num, frac = map(str, Number.split('.'))
    num = int(num, Basein)
    a = toBASEint(num, Baseout)
    b = 0
    k = Basein
    for i in frac:
        b += alpha.index(i) / k
        k *= Basein
    print(a)
else:
    print(toBASEint(int(Number, Basein), Baseout))
