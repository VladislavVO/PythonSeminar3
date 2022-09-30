# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

def random_numbers(min_num:int, max_num:int, size:int):
    return [randint(min_num, max_num) for i in range(size)]
   
numbers:int = random_numbers(1, 10, 10)
print(numbers)

def multiply(numbers:int):
    numbers2= []
    size = 5
    i=0
    while i <=size-1:
        numbers2.append(numbers [i] *numbers [(i+1)*-1])
        i+=1
    return numbers2

final_list = multiply(numbers)
print(final_list)
