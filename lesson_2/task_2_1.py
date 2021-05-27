# Задание 1.Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# решила попробовать еще такой вывод:
print(type(15 * 3) == int)
print(isinstance(15 * 3, list)) #false
print(isinstance(15 * 3, int))
print(isinstance(15 / 3, float))
print(isinstance(15 // 2, int))
print(isinstance(15 ** 2, int))


