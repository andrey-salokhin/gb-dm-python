
#### 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя


def recursive_pow (a, b):
    if b == 0:
        return 1
    return a * recursive_pow(a, b-1)


print(recursive_pow(2, 0))
print(recursive_pow(2, 1))
print(recursive_pow(2, 3))
print(recursive_pow(2, 4))