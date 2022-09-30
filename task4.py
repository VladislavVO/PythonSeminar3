# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

bin = []
def binar(number, n):
    if number == 0:
        return 1
    else:
        bin.insert(n, number%2)  
        return binar(number//2, n-1)

number = binar(int(input('->')), -1)
print (bin)