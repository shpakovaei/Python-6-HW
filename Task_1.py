# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

a = [random.randint (1,21) for _ in range (10)]
print (a)

def unique_numbers(a):
    unique = []

    for number in a:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

unique = unique_numbers(a)

print(unique)

print (len (unique))


