# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи



n = int(input('Введите длину ряда: '))
f1 = f2 = 1
print(f1, f2, end=' ')

i = 2
while i < n:
	f1, f2 = f2, f1 + f2 # f1 приравнивается к f2, f2 приравнивается к f1 + f2
	print(f2, end=' ') # Выводится f2
	i += 1
print()