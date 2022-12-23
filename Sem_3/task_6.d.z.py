# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной 
# части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# 1-й вариант

my_list = [1.1, 1.2, 3.1, 5, 10.01]
listNew = []
difference = 0
numberMax = 0
# numberMin = 6 # Если список элементов задан изначально, то мы присваиваем 
# значение numberMin больше минимального


for item in my_list:
    listNew.append(round(item % 1, 3))
    for item in listNew:
        if item == 0:
            listNew.remove(0)
# print(listNew)
# Находим значение дробной части элементов и добавляем их в новый массив
# Если в новом массиве есть элемент(ы) со значением 0, то удаляем его


for item in listNew:    
    if numberMax < item:
        numberMax = item
# print(numberMax)
# Находим максимальнеое значение дробной части


numberMin = numberMax # Допустим, что список элементов изначально не 
# задан и поэтому мы не знаем минимальное значение элемента массива


for item in listNew:
    if numberMin > item:
        numberMin = item
# print(numberMin)
# Находим минимальнеое значение дробной части


difference = numberMax - numberMin
print(difference)
# Находим разницу между максимальным и минимальным значением дробной 
# части элементов




# 2-й вариант

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# listNew = []
# difference = 0
# numberMax = 0
# numberMin = 0


# for item in my_list:
#     listNew.append(round(item % 1, 3))
#     for item in listNew:
#         if item == 0:
#             listNew.remove(0)
# # print(listNew)
# # Находим значения дробной части элементов и добавляем их в новый массив
# # Если в новом массиве есть элемент(ы) со значением 0, то удаляем его

# numberMax = max(listNew)
# # print(numberMax)
# # Находим максимальнеое значение дробной части

# numberMin = min(listNew)
# # print(numberMin)
# # Находим минимальнеое значение дробной части

# difference = numberMax - numberMin
# print(difference)
# # Находим разницу между максимальным и минимальным значением дробной 
# # части элементов