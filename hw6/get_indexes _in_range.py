#### 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def get_indexes_in_range(genuine_list: list, min: int, max: int) -> list:
    result = []
    for index, value in enumerate(genuine_list):
        if value > min and value < max: result.append((index, value)) 
    return result


print(get_indexes_in_range([randint(1,100) for x in range(50)], 25, 50))
