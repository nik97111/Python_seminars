# Реализуйте алгоритм перемешивания списка.


import random

my_list = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(my_list)
# print(my_list)




from random import sample

listNew = sample(my_list, len(my_list))
print(listNew)




# import numpy as np   #  Если установлен NumPy

# np.random.shuffle(my_list)
# print(my_list)