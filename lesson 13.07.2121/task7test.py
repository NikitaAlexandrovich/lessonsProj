strGC =  input("Введите последовательность: ")
s1 = strGC.upper().count('c'.upper())
s2 = strGC.upper().count('g'.upper())
S = s1 + s2
print(S / len(strGC) * 100)