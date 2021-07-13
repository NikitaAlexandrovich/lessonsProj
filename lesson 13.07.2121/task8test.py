s = str(input("Введите строку: "))
len_str = len(s) - 1
counter = 1
codeStr = ''

if len(s) ==1 :
    codeStr = codeStr + s + str(counter)
else:
    for i in range(0, len_str):
        if s[i] == s[i + 1]:
            counter += 1
        elif s[i] != s[i + 1]:
            codeStr = codeStr + s[i] + str(counter)
            counter = 1
    for j in range(len_str, len_str + 1):
        if s[-1] == s[-2]:
            codeStr = codeStr + s[j] + str(counter)
        elif s[-1] != s[-2]:
            codeStr = codeStr + s[j] + str(counter)
            counter = 1

print(codeStr)