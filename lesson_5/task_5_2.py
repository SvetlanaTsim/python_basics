# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

n = 9
nums_gen = (num for num in range(1, n + 1, 2))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
# print(next(nums_gen)) #StopIteration



# def next_num(num_gen):
#     for num_gen in range(9):
#         print(next(num_gen))
#
# next_num(nums_gen)
