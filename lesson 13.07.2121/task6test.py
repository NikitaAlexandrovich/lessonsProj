def func(x):
    if x <= -2:
        return (1 - pow(x + 2, 2))
    elif -2 < x <= 2:
        return -(x / 2)
    elif x >2:
        return (pow(x - 2, 2) + 1)

print(func(-3))
print(func(2))
print(func(3))