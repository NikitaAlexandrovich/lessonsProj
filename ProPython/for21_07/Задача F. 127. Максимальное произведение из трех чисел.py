import heapq

n = int(input())
str = input()
list_n = str.split()
l = []
for i in list_n:
    l.append(int(i))

x = heapq.nlargest(3, l)
m_index = list()
for i in range(3):
    m_index.append(l.index(x[i]))
m_index.sort()
res = []
for i in range(3):
    res.append(l[m_index[i]])

print(*res)
