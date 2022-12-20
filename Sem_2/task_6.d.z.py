# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и 
# выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число N: '))
my_list = [] 
sumEl = 0


for item in range(1, n + 1):
    my_list.append((item - (1 / item)) ** item)
print(my_list)
for j in range(len(my_list)):
    sumEl += my_list[j]
print('{:.2f}'.format(sumEl))
# d = round(sumEl, 2)
# print(d)
