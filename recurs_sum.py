def sum(x):
    y = x % 10
    x = x // 10
    if x > 0:
        return y + sum(x) #рекурсия
    else:
        return y

print(sum(123456789))
