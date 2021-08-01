def toBASEint(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base]
    while n >= base:
        n = n // base
        b += alpha[n % base]
    return ('' if num >= 0 else '-') + b[::-1]


def toBaseFrac(frac, base, n=16):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n:
        frac *= base
        frac = round(frac, n)
        b += str(alpha[int(frac)])
        frac -= int(frac)
        n -= 1

    print(b)
    b = int(b.rstrip('0').rstrip('A'))
    print(b)
    return b
    # first_pos = {}
    # position = 0
    # period = ""
    # remainder = 1
    #
    # while not (remainder in first_pos):
    #     first_pos[remainder] = position
    #     period += str(remainder // b)
    #     remainder = (remainder % b) * 10
    #     position += 1
    #
    # period = period[first_pos[remainder]:]
    #
    # print(period)
    #
    # return period

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
    b = str(toBaseFrac(b, Baseout)).rstrip('0')
    print(a + '.' + b)
else:
    print(toBASEint(int(Number, Basein), Baseout))
