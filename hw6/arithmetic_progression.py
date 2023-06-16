#### 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии

def arithmetic_progression(condition: list) -> list:
    print(type(condition))
    a1, d, n = condition
    return [a1+(i-1)*d for i in range(1,n+1)]


print(arithmetic_progression([int(input()) for i in range(3)]))