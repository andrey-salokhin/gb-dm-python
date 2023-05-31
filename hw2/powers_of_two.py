####  2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

max = int(input("Enter max number "))

current_number = 1

print(f"{max} ->> , ", end ='')

while (current_number < max):
    print(f'{current_number}, ', end ='')
    current_number*=2

