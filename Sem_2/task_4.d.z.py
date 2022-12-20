# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


#  1-й вариант. Выполнение через строку для всех вещественных 
# чисел (целых и дробных). 

# number = float(input('Введите число дробное или больше 10: '))
# sumDigits = 0

# for item in str(number):
#     if item != ".":
#         sumDigits += int(item)
# print(sumDigits)



# 2-й вариант. Выполнение для целых чисел 

# number = float(input('Введите число дробное или больше 10: '))
# sumDigits = 0

# while number > 0:
#     sumDigits += number % 10
#     number //= 10
# print(sumDigits)



# 3-й вариант. Выполнение для дробных чисел (только аналогично 0.56). 
# Решение неверное 

# number = float(input('Введите число дробное или больше 10: '))
# sumDigits = 0
# i = 0
# j = 0

# while  0 < number < 1:
#     number *= 100
#     i = number % 10
#     j = number // 10
#     sumDigits += i + j
# print(sumDigits)
