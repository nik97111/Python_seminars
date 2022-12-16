#2. Напишите программу, которая на вход принимает 5 чисел и находит 
# максимальное из них.
    #Примеры:
    # - 1, 4, 8, 7, 5 -> 8
    # - 78, 55, 36, 90, 2 -> 90


# 1-й вариант. С изначально заданными значениями

# my_list = [23, 54, 76, 99, 32]
# numberMax = 0

# for num in my_list:
#     if num > numberMax:
#         numberMax = num
# print(numberMax) 



# 2-й вариант. Например, есои нам нужен массив с введенными числами
# для дальнейших действий

numberMax = 0
my_list = []
for _ in range(5):
    number = int(input('Введите число: '))
    my_list.append(number)
print(my_list)
 
for num in my_list:
    if num > numberMax:
        numberMax = num
print(numberMax) 



# 3-й вариант

# numberMax = 0
# for i in range(5):
#     number = int(input('Введите число: '))
#     if number > numberMax:
#         numberMax = number
# print(numberMax) 


# 4-й вариант. С функцией

# def getNumbers(number):
#     my_list = []
#     numberMax = 0

#     for i in range(number):
#         number = int(input('Введите число: '))
#         my_list.append(number)
#         if number > numberMax:
#             numberMax = number
#     return my_list, numberMax

# my_list, numberMax = getNumbers(5)
# print(numberMax)


# 5-й вариант. С функцией max

# my_list = [23, 54, 76, 99, 32]
# print(max(my_list)) 


# my_list = []
# for _ in range(5):
#     my_list.append(int(input('Введите число: ')))
# print(max(my_list)) 
