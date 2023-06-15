

#### 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя

def recursive_sum(a, b):
        current_result = 0

        if a == 0 and b == 0:
            return 0
        if a == 0: 
             temp_a = 0
        else:
             temp_a = a - 1
             current_result += 1

        if b == 0:
             temp_b = 0
        else:
             temp_b = b - 1
             current_result += 1

        return current_result + recursive_sum(temp_a, temp_b)
              
print(recursive_sum(8,7))