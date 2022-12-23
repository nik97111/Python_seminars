# Напишите программу, которая будет преобразовывать десятичное число в 
# двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# 1-й вариант

N = int(input('Введите число N: '))
my_list = []

while N:
    my_list.append(N % 2)
    N //= 2
my_list.reverse()
print(my_list)


# 2-й вариант

# number = int(input('Введите положительное число: '))
# print(bin(number))
