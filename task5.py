# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Input k:'))

def neg_fib(number):
	negative_fib = []
	f1 = 1
	f2 = -1
	for i in range(number+1):
		if i ==0: negative_fib.insert(i, f1) 
		elif i ==1: negative_fib.insert(i, f2) 
		else:
			negative_fib.insert(i, f1-f2) 
			x=f2
			f2=f1-f2
			f1=x
	return negative_fib

negative_fib = neg_fib(number)	


def pos_fib(number):
	positive_fib = []
	f1 = 0
	f2 = 1
	for i in range(number+1):
		if i ==0: positive_fib.insert(i, f1) 
		elif i ==1: positive_fib.insert(i, f2) 
		else:
			positive_fib.insert(i, f1+f2) 
			x=f2
			f2=f1+f2
			f1=x
	return positive_fib

positive_fib = pos_fib(number)	


fib = str(negative_fib[::-1]+positive_fib)
print(fib)