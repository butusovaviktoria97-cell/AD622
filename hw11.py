# d = {
#     "John":{
#         'N':3056,'S':8463,'E':8441,'W':2694
#     },
#     "Tom":{
#         'N':4832,'S':6786,'E':4737,'W':3612
#     },
#     "Anne":{
#         'N':5239,'S':4802,'E':5820, 'W':1859
#     },
#     "Fiona": {
#         'N': 3904,'S': 3645,'E': 8821,'W': 2451
# }
# }
# # print(d)
# print("Исходные данные: ")
# for name, reg_1 in d.items():
#     print(name)
#     for reg_2 in d[name]:
#         print("\t",reg_2, ": ", d[name][reg_2], sep="")
#
# name = input("Введите имя продавца: ")
# region1 = input("Введите регион (N/S/E/W): ")
# sales = d[name]
# print("Текущее значение для",name)
# for r, v in sales.items():
#     print(r,":",v)
#
# new_value = int(input("Введите новое значение: "))
#
# sales[region1] = new_value
#
# print("\n Обновленные продажи для", name)
# for reg, val in sales.items():
#     print(reg, ":",val)\

# for i in range(-2):
#     print(i)

# num = float(2)
# print(num)

import random
print(random.randint())


