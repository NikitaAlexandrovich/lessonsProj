n = int(input())
mas = []
if n == 1:
    print("1:1")
else:
    while n > 1:
        i = 2
        f = 0
        while True:
            if n % i == 0:
                n = n // i
                mas.append(i)
                f = 1
                break
            else:
                i += 1
        if f == 1:
            continue
    res = {i: mas.count(i) for i in mas}
    r = ','.join(['{}:{}'.format(k,v) for k,v in res.items()])
    print(r)

    # result = list(mas.count(i) for i in mas)
    # newlist = []
    # for i in mas:
    #     if i not in newlist:
    #         newlist.append(i)
    #
    # print(newlist)
    #
    # new = []
    # for i in result:
    #     if i not in new:
    #         new.append(i)
    # print(new)
    # str = ''
    # for i in newlist:
    #     str = str + str(i) + ":" + str()
