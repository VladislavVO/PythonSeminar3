# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

# numbers:int = [1.1, 1.2, 3.1, 5.17, 10.02]
# print (numbers)

# numbers2= []
# for i in numbers:
#     numbers2.append(int(str(i).split('.')[1]))
# print (numbers2) 

# # def find_dif(numbers2):
# #     dif = 0
# #     # maxim = max(numbers2)
# #     # minim = min(numbers2)
# #     print (maxim, minim)
# #     if int(maxim) < 10:
# #         maxim = int(maxim) * 10
# #         dif = int(maxim) - int(minim)
# #     print(dif)
# #     return dif

# def find_dif(numbers2):
#     i=0
#     if int(numbers2[i]) < 10:
#         numbers2[i] = 5
#             # numbers2.append(numbers2 [i] * 10)
#         i+=1
#     return numbers2
# print (numbers2) 


# find_dif(numbers2)

nums = [1.1, 1.2, 3.1, 5.17, 10.01]

def null_counter(num:float):
    counter = 0
    while num != int(num):
        num*=10
        counter+=1
    return counter, num

def change_list(nums: list):
    max_counter = 0
    counters_list = []
    for i in range(len(nums)):
        counter, num = null_counter(nums[i])
        counters_list.append(counter)
        nums[i] = num
        if counter > max_counter:
            max_counter =  counter
    for i in range(len(counters_list)):
        counter = max_counter - counters_list[i]
        if counter:
            nums[i]*=10**counter
    return nums, max_counter

def dif_max_min(nums: list):
    nums, max_counter = change_list(nums)
    print(nums, max_counter)
    max_num, min_num = 0, nums[0]
    for num in nums:
        float_part = num%10**max_counter
        print(float_part)
        if float_part> max_num:
            max_num=float_part
        if float_part< min_num:
            min_num=float_part
    print(f'{max_num=},{min_num=}')
    return max_num - min_num, (max_num-min_num)/10**max_counter

print (dif_max_min(nums))




