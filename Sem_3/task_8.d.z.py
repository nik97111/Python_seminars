# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# 1-й вариант

N = int(input('Введите число: '))
my_list = [0, 1]
numFb1 = 0
numFb2 = 1
listNew = []

for item in range(2, N + 1):
    numFb1, numFb2 = numFb2, numFb1 + numFb2
    my_list.append(numFb2)
print(my_list, end=', ')




# 2-й вариант

# def fibonacci(N):
#     if N in (1, 2):
#         return 1
#     return fibonacci(N - 1) + fibonacci(N - 2)
 
# print(fibonacci(8))