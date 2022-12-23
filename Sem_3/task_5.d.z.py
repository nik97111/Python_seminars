# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
listNew = []

for i in range(len(my_list)):
    listNew.append(my_list[0] * my_list[-1])
    del my_list[0]
    del my_list[-1]
    if len(my_list) == 1:
        listNew.append(my_list[0] ** 2)
        del my_list[0]
    if len(my_list) == 0:
        break
print(listNew)


