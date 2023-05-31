#### 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

number_of_coins = int(input("Введите количество монет: "))
string_of_sides = ""
eagle_counter = 0
tails_counter = 0

for coin in range(number_of_coins):
    current_side = input(f"Введите 0 или 1 для {coin + 1} монеты ")
    while current_side != '0' and current_side !='1':
        print('Неверный ввод, повторите попытку')
        current_side = input(f"Введите 0 или 1 для {coin + 1} монеты ")
    if current_side == '0':
        eagle_counter+=1
    else:
        tails_counter+=1
    string_of_sides += current_side

print(string_of_sides)
print (f'Кол-во монет, чтобы перевернуть: {eagle_counter}') if eagle_counter <= tails_counter else print(f'Кол-во монет, чтобы перевернуть: {tails_counter}')