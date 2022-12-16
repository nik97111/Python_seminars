# 5. Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не 30.


# 1-й вариант

number = int(input('Введите число: '))
if (((number / 5 and number / 10 or number / 15) >= 1) and number / 30 != 1):
    print('да')
else:
    print('нет')


# 2-й вариант

# number = int(input('Введите число: '))
# if (((number % 5 and number % 10 or number % 15) == 0) and number % 30 != 0):
#     print('да')
# else:
#     print('нет')



# 3-й вариант. Как в семинаре

# number = int(input('Введите число: '))
# if ((number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0):
#     print('да')
# else:
#     print('нет')