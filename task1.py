# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint

def random_numbers(min_num:int, max_num:int, size:int):
    return [randint(min_num, max_num) for i in range(size)]
   
numbers = random_numbers(1, 20, 7)
print(numbers)

def summa_numbers (numbers2):
    sum: int = 0
    for i in numbers2:
        sum = sum + i
    return sum

numbers2=numbers[1::2]
print (numbers2)
print (summa_numbers(numbers2))