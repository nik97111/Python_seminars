# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
my_list = [] 

for item in range(-N, N + 1):
    my_list.append(item)
print(my_list)

my_data = open('file_7.d.z.txt', 'w')
my_data.writelines(str(my_list))
my_data.close()