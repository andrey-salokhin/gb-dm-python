#### 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.

import math

b = abs(int(input('Введите сумму ')))
c = abs(int(input('Введите второе число ')))

discriminant = b * b - 4 * c

if discriminant >= 0:
    x2 = (-b - math.sqrt(discriminant))/2
    x1 = (-b + math.sqrt(discriminant))/2
    print (f'{b} {c} > {x1} {x2}')

