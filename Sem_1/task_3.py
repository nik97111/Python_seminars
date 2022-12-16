# 3. Напишите программу, которая будет на вход принимать число N и 
# выводить числа от -N до N
    # *Примеры:* 
    # - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# 1-й вариант

N = int(input('Введите число: '))

for num in range(-N, N + 1):
    print(num, end= ', ')


# 2-й вариант

# N = int(input('Введите число: '))
# my_list = []

# for num in range(-N, N + 1):
#     my_list.append(num)
# print(*my_list)


# 3-й вариант

# N = int(input('Введите число: '))
# my_list = range(-N, N + 1)
# print(*my_list)
# print(type(my_list))

# print (list(my_list))
