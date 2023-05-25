# Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод.

num = int(input('Enter your number: '))
stringed_number = str(num)

sum = 0

while num > 0:
    sum +=  num % 10
    num //= 10 

divided_number = f'{stringed_number[0]}'
for digit in stringed_number[1:]:
    divided_number += f' + {digit}'


print(f'Сумма числел числа {stringed_number} равна {sum} ({divided_number})')  
