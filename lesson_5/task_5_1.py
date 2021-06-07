# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def num_generator(n):
    for num in range(1, n+1, 2):
        yield num

num_15 = num_generator(15)
print(next(num_15))
print(next(num_15))
print(next(num_15))
print(next(num_15))
print(next(num_15))
print(next(num_15))
print(next(num_15))
print(next(num_15))
print(next(num_15)) #StopIteration





