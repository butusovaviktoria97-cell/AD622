# num = 97531
# one = num % 10 # получили 1
# num = num // 10 # 9753
# two = num % 10 # получили 3
# num = num // 10 # 975
# three = num % 10 # получили 5
# num = num // 10 # 975
# four = num % 10 # получили 7
# num = num // 10 # 9
# five = num % 10 # получили 9
# mul = one * two * three * four * five # 945
# print('Произведение чисел:', mul)
# sum = (one + two + three + four + five)/ 5
# print('Среднее арифметическое:', sum)
from os import remove

# # str1 = 'Привет, хозяин!' # длина
# str2 = len(str1)
# print(str1)
# print(str2)

# индексирование:
# str1 = 'Привет, хозяин!'
# print(str1[2]) # расчет от нуля

# нарезка (слайсинг):
# str1 = 'Привет, хозяин!'
# print(str1[0:6]) # извлекли привет

# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not b)

# a = 30
# b = 20
# print(a == b)
# print(a != b)

# a = 5
# b = 5
# sum1 = a+b
# print(type(sum1))
# print(sum1)
# sum1 = float(sum1)
# print(type(sum1))
# print(sum1)

# a = 37
# res = a % 2
# print(res)

# i = 1
# while i < 6:
#     print(i, end=' ')
#     i += 1
# print()
# i = 1
# while i < 6:
#     print(i * 2, end=' ')
#     i += 1

# n = int(input("Введите число: "))
# i = 1
# while i <= n:
#     print('Hello')
#     i += 1


# i = 20
# while i >= 10:
#     print(i)
#     i -= 1

# guess = input("Введите пароль: ")
# password = 'qwerty'
# cou = 0
# while guess != password:
#     if cou < 5:
#         cou = cou + 1
#         print("Неправильный пароль! Повторите попытку ", "Выполнено попыток: " ,cou)
#         guess = input("Введите пароль повторно: ")
#     else:
#         print("Логин заблокирован! ")
#         break
#
a = [1, 2, 3] * 3
# print(a)
# # a.remove(3)
# # print(a)
while 3 in a:
    a.remove(3)
print(a)

# s = "Привет"
# while len(s) > 0:
#     print(s[0])
#     s = s[1:]
#
# a = int(input("Введите кол-во символов:" ))
# b = input("Введите символ:" )
# c = int(input("Введите ориентацию, где 0 - горизонтальная, 1 - вертикальная: "))
# i = 0
# while i < a:
#     if c == 0:
#
#         print(b, end=' ')
#     if c == 1:
#         print(b)
#     i += 1








