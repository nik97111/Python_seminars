# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.



#  1-й вариант. Если заранее заданы значения обеих строк

# str1 = 'kolertsykolubgdkoldswkolgf'
# str2 = 'kol'
# count = 0
# for i in range(len(str1)):
#     if str2[0] == str1[i] and str2[1] == str1[i + 1] and str2[2] == str1[i + 2]:
#         count += 1
# print(count)



# 2-й вариант

# str1 = 'kolertsykolubgdkoldswkolgf'
# str2 = 'kol'
# print(str1.count(str2))





# str1 = 'kolertsykolubgdkoldswkolgf'
# str2 = 'kol'
# count = 0

# for i in range(len(str1) - len(str2)):
#     if str2 == str1[i: i + len(str2)]:
#         count += 1
            
# print(count)



# str1 = 'kolertsykolubgdkoldswkolgf'
# str2 = 'kol'
# count = 0
# for i in range(len(str1) - len(str2)):
#     if str2[0] == str1[i]:
#         for j in range(1, len(str2)):
#             if str2[j] != str1[i + j]:
#                 break
#         else:
#             count += 1
# print(count)

str1 = 'kolertsykolubgdkoldswkolgf'
str2 = 'kol'
count = 0
for i in range(len(str1)):
    if str2[0] == str1[i]:
        for j in range(1, len(str2)):
            if str2[j] != str1[i + j]:
                break
        else:
            count += 1
print(count)



