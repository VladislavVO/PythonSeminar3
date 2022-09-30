# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

numbers:int = [1.1, 1.2, 3.1, 5.17, 10.02]
print (numbers)

numbers2= []
numbers3= []
numbers4= []
for i in numbers:
    numbers2.append(int(str(i).split('.')[1]))

    numbers3:int = numbers2
    numbers4.append(numbers [i] - numbers [i])

print (numbers2) 
print (numbers3) 
print (numbers4) 

def find_max(numbers2):
    max=numbers(0)
    
    return max

print(max(numbers2))  