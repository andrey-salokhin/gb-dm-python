#### 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

bushes = [1, 2, 3, 4, 5, 6, 7, 8]
bushes = [11, 92, 1, 42, 15, 12, 11, 81]

result = 0
bush_number = -1

for i in range(len(bushes)):
    if i == 0:
        current_result = bushes[-1] + bushes[i] + bushes[i+1]
        if current_result > result:
            result = current_result
            bush_number = i + 1
    elif i == len(bushes) - 1:
        current_result = bushes[i-1] + bushes[i] + bushes[0]
        if current_result > result:
            result = bushes[i] + bushes[i-1]
            bush_number = i + 1
    else:
        current_result = bushes[i-1] + bushes[i] + bushes[i+1]
        if current_result > result:
            result = current_result
            bush_number = i + 1

print(f'Макс. кол-во ягод {result}, собрано для куста {bush_number}')