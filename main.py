# print("hello world")
# print("Привет мир")
# name = "admin"
# import doctest
# from _pyrepl import keymap
# from doctest import script_from_examples
# from operator import truediv
# from pickletools import read_stringnl_noescape
# from queue import PriorityQueue
from sqlite3 import dump

# print("Hello,", name, type(name), id(name))
# age = 20
# print(age, type(age), type(age), id(age))

# a = b = c = 1
# print(a, b, c)
# print(id(a), id(b), id(c))

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# import keyword
# print(keyword.kwlist)
#
# a = 1
# b = 5
# print ("a:", a)
# print ("b:", b)
# # c = a # 1
# # a = b # 5
# # b = c # 1
# a, b = b, a # так работает только в питоне
# print ("a:", a) # 5
# print ("b:", b) # 1

# print("Hello \
# World")
# print('Hello \nWorld')
# print("\tДокумент \"script.py\" находится по заданному пути\r D:\\folder\\file\\script.py")
# s1 = ('Hello')
# s2 = ('World')
# s3 = s1 + ", " + s2 + '!\t\t'# конкатенация строк
# print(s3 * 5)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 // 4)
# print(6 ** 3)
# print(7 % 2) # остаток от деления, проверять число на четность

# number = 6 + 4 * 5 ** 2 + 7
# print(number) # 113

# num = 10 # оператор присваивания
# # num = num + 5
# num += 5
# print(num) #15
#
# num -=3 # num = num - 3
# print(num)
#
# num *= 4
# print(num)

# Дано 4х значное число - развернуть в противополож. последовательности:
# num = 4321
# print("Исходное число:", num)
# one = num % 10 # 1
# num = num // 10 # 432
# two = num % 10 # 2
# num = num // 10 # 43
# three = num % 10 # 3
# num = num // 10
# four = num % 10  #4
# res = one * 1000 + two * 100 + three * 10 + four
# print('Обратное число:', res)

# num = 4321
# res = num % 10 * 1000
# num = num // 10
# res +=
# print("обратное число:" res) .....

# num1 = '2'
# num2 = 3
# # res = int(num1) + num2 # 5 сумма
# res = num1 + str(num2) # 23 конкатенация
# print(res)

# print(int(3.8)) # отбросили дробную часть
# print(round(3.891, 2)) # округление по законам математики
# print(type(round(3.891, 2)))

# num1 = '2.5'
# num2 = 3
# result = float(num1) + num2 # 2.5 + 3
# print(result)

# one = 1
# two = 2
# print('one:', one, '\ntwo:', two)

# name = 'Виктор'
# age = 20
# # print('меня зовут', name, '.Мне', age, 'лет.')
# # print('меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print('меня зовут ', name, '. Мне ', age, ' лет.', sep='', end='\n\n')
# print('я учу Python')
#
# name = input("Введите имя: ")
# print('Ваше имя:', name)

# num = int(input('Введите число: '))
# power = int(input('Введите степень: '))
# num = int(num)
# power = int(power)
# # print(type(num))
# res = num ** power
# print(res)

# b1 = True # 1
# b2 = False # 0
# # print(b1, type(b1))
# # print(b2, type(b2))
# print(b1 + 5) # 1 + 5
# print(b2 + 5) # 0 = 5

# print(bool('Python'))
# print(bool(None))

# print(7 == 7)
# print(2 + 5 == 7)
# print(3 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 < 5)
# print(8 <= 5)
# print(9 >= 9)
# print('привет' > 'ПРИВЕТ')

# print(2 < 4 < 9) # True True
# print(2 * 5 > 7 >= 4 +3) # True True 10 > 7 >= 7
# print(3 * 3 <= 7 >= 2) # False True 9 <= 7 >= 2 итог False

# a = 10
# b = 5
# c = a == b
# print(a, b, c) # 10 5 False


# print (not 9 - 9)
# print(5 - 3 == 2 and 1 + 3 == 4) # 2 == 2 true , 4 == 4 true/ true
# print(5 - 3 == 2 and 1 + 3 < 4) # 2 == 2 true , 4 < 4 false/ false
# print(5 - 3 >  2 and 1 + 3 == 4) # 2 > 2 false , 4 == 4 true/ false
# print(5 - 3 >  2 and 1 + 3 < 4) # 2 > 2 false , 4 < 4 false/ false
#
# print(5 - 3 == 2 or 1 + 3 == 4) # 2 == 2 true , 4 == 4 true/ true
# print(5 - 3 == 2 or 1 + 3 < 4) # 2 == 2 true , 4 < 4 false/ true
# print(5 - 3 >  2 or 1 + 3 == 4) # 2 > 2 false , 4 == 4 true/ true
# print(5 - 3 >  2 or 1 + 3 < 4) # 2 > 2 false , 4 < 4 false/ false

# cnt = 5
# if cnt < 10: # 5<10, true
#     cnt +=1
# print(cnt)

# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешен')
# else: # иначе
#     print('Доступ запрешен')

# a  = 25
# b = 15
# if a > b:
#     print('a > b')
# if a < b:
#     print('b > a')
# else:
#     print('a == b')
#
# a  = 0
# b = 15
# if a > b:
#     print('a > b')
# if a < b:
#     print('b > a')
# if a == b:
#     print('a == b')
#
# if a > b:
#     print('a > b')
# elif a < b:
#     print('b > a')
# else:
#     print('a == b')

# a = input('Введите сторону а: ')
# b = input('Введите сторону b: ')
# c = input('Введите сторону c: ')
# if a == b or b == c or c == a:
#     print('Треуголник равнобедренный')
# elif a == b == c:
#     print('Треуголник равносторонний')
# else:
#     print('Треуголник разносторонний')

# программа по выводу месяца
# a = int(input('Введите месяц(цифровой): '))
# if 1 <= a <= 12:
#     if a == 1 or a == 2 or a == 12:
#         print('зима - ')
#     if 3 <= a <= 5:
#          print('весна')
#     if 6 <= a <= 8:
#         print('лето')
#     if 9 <= a <= 11:
#         print('осень')
# else:
#     print('Ошибка ввода данных')
#
# 20.06.26
# a, b = 10, 20
# print(a if a< b else b)

# a, b = 30, 40
# print("a == b" if a==b else "a > b" if a > b else "a < b")

# try:
#     n = int(input("Введите целое число:"))
#     print(n * 2)
# except ValueError:
#     print("Что то пошло не так")
#

# try:
#     n = int(input("Введите делимое:"))
#     m = int(input("Введите делитель:"))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')

# try:
#     n = int(input("Введите делимое:"))
#     m = int(input("Введите делитель:"))
#     print(n / m)
# except ValueError, ZeroDivisionError:
#     print('Нельзя вводить строки или делить на ноль')
# else: # когда в блоке try  не возникло исключение
#         print("Все нормально, Вы ввели числа", n, "и", m)
# finally: # выполнится в любом случае
#         print('Конец программы')
#
# n = input('Введите первое число:') # "2"
# m = input('Введите второе число:')# "WWW"
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n) # опять строка
#     m = str(m) #  это можно не указывать
# finally:
#     print(n + m)

# Цикл: повторять одно и тоже действие несколько раз, консрукция повторения
# # # while #  используется когда мы заранее не знаем сколько итераций произойдет
# # итерация - один шаг цикла
# i = 0  # переменная ссчеткик
# while i < 5: #   пока 0 меньше 5
#     print('i=',i)
#     i += 1 # чтобы цикл когда нибудь закончился. Переменнаая счетчик,
#     # чтобы изменять
#     # нашу переменную для того чтобы цикл когда нибудь законнчился

# i = 10
# while i > 0:
#     print('i =', i)
#     i -=1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 1

# i = 2 # второй вариант
# while i <= 20:
#     print(i, end=' ')
#     i += 2

# n = int(input('Укажите кол-во символов: '))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1
#

# n = int(input('Укажите кол-во символов: '))
# while n > 0:
#     print('*', end='')
#     n -= 1

# n = int(input('Введите начало диапазона: '))
# m = int(input('Введите конец диапазона: '))
# sum1 = 0
# i = n
# while i <= m:
#     sum1 = sum1 + i
#     i = i + 2
# print(sum1)
#
#
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# summa = 0
#
# if start % 2 == 0:
#     start += 1
#
# while start <= end:
#     summa += start
#     start += 2
#
# print("Сумма нечетных чисел =", summa)

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
# res = 0
# while start <= end:
#     if start % 2 != 0: # или  start % 2: или  start % 2 == 1:
#         res += start
#     start += 1
# print(res)

# задача
# n = input('введите целое число: ')
#
# while type(n) is not int: # аналог is not =!
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число:")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i,end=" ")
#     if i ==5:
#         break #  полностью прерывает итерацию
#     i += 1
# print("\nЦикл заыершен")
#
# i = 0
# while True:
#     print("i=", i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n  # res = res * n
#
# print("Результат: ",res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Done", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i = ",i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j = ",j)
#         j += 1
#     i += 1

# 21.6.26

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j,"=",i * j, end="\t\t")
#         j += 1
#     print()
#     i +=1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
# print(element)

# for i in "red", "orange", "yellow": # каждый элемен можно взять отдельно
#     print(i)


# for i in range(2, 9, 3): #   начиная с нуля по умолчанию. start, stop, step
#     print(i, end=" ")
#
# print()
#
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3

# for i in range(9, 0, -1): #   начиная с нуля по умолчанию. start, stop, step
#     print(i, end=" ")
#
# print()
#
# j = 9
# while j > 0:
#     print(j, end=" ")
#     j -= 1

# for i in range(10,100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("else")


# for i in range(4):
#     for j in range(12):
#         print("*", end=" ")
#     print()


# for i in range(4):
#     for j in range(16):
#         if i == 0 or j == 0 or i == 3 or j == 15:
#           print("*", end="")
#         else:
#                 print(" ", end="")
#     print()
#
# run = [i * 2 for i in "hello"]
# print(run)


# run = [i for i in range(10) if i % 2 == 0]
# print(run)
#
# nums = [8, 3, 9, 4, 1] #  список
#      # 0  1   2  3  4
#      # -5 -4 -3 -2 -1
# print(nums)
# # print(nums [0]) #  обращение по индексу, начинаяя с нулевого
# # print(nums [-5]) #  обращение по индексу, начинаяя с нулевого
# #
# # nums[-1]  = 256
# # nums[3]  += 100
# # print(nums)
#
# print("Длина списка:", len(nums))

#  способы создания списка:
# s = [1, 3, 5]
# print(s * 3, type(s))
#
# b = list("Helo")
# print(b, type(b))

# n = list(range(10, 2, -2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a [int] = int(input("->"))
# print(a)

# a = [int(input("->")) for _ in range(int(input("n= ")))] # range (0,5)
# print(a)

#
# a = [9, 7, 6, 1, 2]
#
# for i in range(len(a)): # i = 0, 1,2,3,4
#     print(a[i], end=" ") #  9, 7, 6, 1, 2
#
# print()
#
# for el in a: # el =  9 7 6 1 2
#     print(el, end=" ")

# a = [int(input("->")) for _ in range(int(input("n= ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("сумма отриц элементов: ", s)
#


# a = [int(input("->")) for _ in range(int(input("n= ")))]
# print(a)
# s = 0
# for i in a:
#     if i < 0:
#         s += i
#
# print("сумма отриц элементов: ", s)



# a = [int(input("->")) for _ in range(int(input("n= ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] >a [i - 1]:
#         print (a[i], end=" ")
# print("сумма отриц элементов: ", s)

# n = list (range(21,41))
# print(n)
# k = s = 0
# for i in range (len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Кол-во четных эл списка: ",k)
# print("Сумма нечет эл: ",s)


#
# n = list (range(21,41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Кол-во четных эл списка: ",k)
# print("Сумма нечет эл: ",s)

# a = [7,9,2,1,3]
# a[0], a[1] = a[1], a[0]
# print(a)

# # Срезы:
# # список [start: stop: step]
# a = [7, 9, 2, 1, 3, 8]
# # 0,1,2,3,4,5 - индексы
# # длина списка 6
# print(a, len(a))
# print(a[::])
# print(a[1::2])
# print(a[5::-1])
# print(a[10:20])

#
# создать срезы из списка [1, 2, 3, 4, 5, 6, 7]
# n = list(range(1,8))
# # print(n) # [1, 2, 3, 4, 5, 6, 7]
# print(n[-1::-1]) # [7, 6, 5, 4, 3, 2, 1]
# print(n[6::-1]) #  [7, 6, 5, 4, 3, 2, 1]
# print(n[::2]) #  [1, 3, 5, 7]
# print(n[1::2]) #  [2, 4, 6]
# print(n[:1:]) #  [1]
# print(n[-1::]) # [7]
# print(n[3:4:]) # [4]
# print(n[4::]) # [5, 6, 7]
# print(n[4:1:-1]) # [5, 4, 3]
# print(n[2:5:]) # [3, 4, 5]

#27.06.2026
# a = [7, 9, 2, 1, 3, 8]
# print(a, len(a))
#
# print(a[1:3])
# a[1:3] = [0,0,0,0]
# print(a, len(a))
# a[1:2] = [20]
# print(a, len(a))
#
#методы списка
# print(dir(list))
# a = [7, 9, 2, 1, 3, 8]
# print(a)
# #append - добавляет элемент в конец списка
# a.append(5)
# print(a)
# #extend - добавляет элементы в конец списка
# a.extend([1,2,3])
# print(a)
# #insert - добавляет элемент в какой то индекс сдвигая ряд
# a.insert(-1, 100)
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(num, x)
# print(s)

# a = [1, 2, 3]
# b = [11 , 22, 33]
# c = []
# for i in range(len(a)): # цикл состоит из трех итераций, т.к. мы его ограничили длиной списка= 3
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [1, 7, 9, 2, 1, 3, 8, 1]
# print(a)
# # del a[0] # удаляет по индексу
# # print(a)
# #
# # a[3:] = [] # за счет добавления пустого списка произойдет удаление
# # print(a)
# #
# # a.remove(1) # удаление по значению (поаторные не удалит)
#
# # last = a.pop(-2) #удаляет последний элемент  списка или по конкретному индексу
# # print(last) # возращает удалчемый элемент, чтобы использовать
# # print(a)
#
# # b = a.count(9) #посмотреть сколько раз встречается элемент списка
# ch = 7
# if ch in a: # есть ли число 6 в списке a
#      b = a.index(ch)
#      print(b)
#
# a = [1, 7, 9, 2, 1, 3, 8, 1]
# print(a)
#
# a.clear() # очищает список
# print(a)

#
# a = [1, 7, 9, 2, 1, 3, 8]
# print(a)
# new_list = a.copy()
# print(new_list)
# new_list.append(400)
# print(new_list)
# print(a)

# a.reverse() # разварачивает список
# print(a)

#
# a = [1, 7, 9, 2, 1, 3, 8]
# print(a)
# lst = list(reversed(a)) #не меняет исходный, а новый разворачивается
# print(lst)
# print(a)
# lst.append(100)
# print(lst)
# print(a)


# a = [1, 7, 9, 2, 1, 3, 8]
# print(a)
# a.sort(reverse=True) #сортировка по убыванию
# print(a)
#
# lst = ["Виталий", "Сергей", "Александр", "Анна"]
# print(lst)
# # lst.sort() # по алфавиту
# # print(lst)
# # lst.sort(key=len, reverse=True) # сортировка по длине
# new_lst = sorted(lst, key=len, reverse=True) # по алфивиту
# print(new_lst)
# # print(lst)
# # sort  - это метод сортировки списка, изменчют исходный список
# # sorted - встроенная функция,не изменяют исходный список

# import random # 1 вариант
# print(random.random())
# print(random.randint(1, 9)) # включает 9
# print(random.randrange(1, 9, 2)) # stop не включает 9

# import random as rnd # 2 вариант с указанием псевдонима
# print(rnd.randint(1, 9)) # включает 9
# print(rnd.randrange(1, 9, 2)) # stop не включает 9

# from random import randrange, randint # 3 вариант(преимущественный) с указанием элемента который хотим использовать
# print(randint(1, 9)) # включает 9
# print(randrange(1, 9, 2)) # stop не включает 9


# from random import * # 4 вариант встраивает весь документ random вес загрузки будет больше
# print(randint(1, 9)) # включает 9
# print(randrange(1, 9, 2)) # stop не включает 9
#
# import random as rnd
# # city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(rnd.choice(city_list)) # сгенерировать случайное значение из нашего списка
# print(rnd.choices(city_list, k=2)) # список с указанным кол-вом элементов 2 значения из списка
# rnd.shuffle(city_list) # перемешивает случайным образом список
# print(city_list)

# import random as rnd
# lst = [rnd.randrange(0, 100) for i in range(10)] # от нуля до 100(не включая 100) 10 чисел
# print(lst)

#
# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(min(lst)) # минимальное значение в списке
# print(max(lst)) # макс значение в списке
# print(sum(lst)) # сумма списка
#
# import random
# lst = [random .randint(0, 100) for i in range(10)] # от нуля до 100  10 чисел
# print(lst)
# maximum = max(lst)
# print("max=", maximum)
# lst.remove(maximum) # удалили из списка
# lst.insert(0, maximum) # переместили на нулевой индекс
# print(lst)

# матрицы - список может лежать внутри другого списка
# matrix = [
#     [1,2,3,4],# 0 индекс
#     [5,6,7,8], # 1 индекс
#     [9,10,11,12] # 2 индекс
# ]
# print(matrix)
# # print(len(matrix))
# # print(matrix[1][2])
#
# # ============================
#
# for row in range(len(matrix)): # в row находятся индексы основного списка
#     # print(matrix[row])
#     for col in range(len(matrix[row])): # в col индексы вложенного списка
#         print(matrix[row][col], end="\t")
#     print()
# print()
# # ============================
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))
# print(math.pi)

# def hello(name, word): # функция , обращаемся к ее имени. name - принимаемый аргумент
#     print("Hello, ", name, ". Say ", word, sep='')
#
# hello("Irina", "Hi")# параментры
# hello("Ivan", "Hello")

# def get_sum(a, b):
#     print("Сумма:", end=" ")
#     return a + b # прерывает выполнение функции, все что ниже не будет отрабатывать
#
# x = 2
# y = 5
# res = get_sum(x,y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
# print(maximum(9,6))


# def maximum(one, two):
#     if one > two:
#         return one
#     return two
#
#
# print(maximum(9,16))

# поиск числа в кубе
# def cube(a):
#     return a**3
#
# for i in range(1, 11):
#     print(i, "в кубе= ", cube(i))

#======
#функция которая принимает список и меняет его первый и последний элемент. В списке мин 2 элеме
# нта
# 1 вариант:
# def change(lst):
#     last= lst.pop() # удалили последний элемент списка
#     first = lst.pop(0)# удалили элемент с нулевым индексом
#     lst.insert(0,last)
#     lst.append(first)
#     return lst
#
# print(change([1,2,3,]))
# print(change([9,12,33, 105]))
# print(change(["с","л","о","н"]))
#
# # 2 вариант
# def change(lst):
#    lst[0], lst[-1] = lst[-1], lst[0]
#    return lst
#
# print(change([1,2,3,]))
# print(change([9,12,33, 105]))
# print(change(["с","л","о","н"]))

#========================================================================
# 05.07.2026
# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a,b,c = 0,d= 1): # d= 1 аргумент со значением по умолчанию
#     return a+b+c+d
# print(get_sum(1,5,2,7))
# print(get_sum(1,5,2,))
# print(get_sum(1,5, 2))
# print(get_sum(1,5, d=2)) # 8 именованный параметр
# print(get_sum(1,5, d=2)) # 8 именованный параметр
# print(get_sum(a = 3, b=1,  d=2,c=5,)) # именованный параметр

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, end="\n\n")
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")


#==========
# крестики нолики:
# board = [" "] * 9 # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# game_over = False
# player = "X"
#
#
# def show():
#      print(board[0]+ " | " + board[1] + " | " + board[2])
#      print("- + - + -")
#      print(board[3] + " | " + board[4] + " | " + board[5])
#      print("- + - + -")
#      print(board[6] + " | " + board[7] + " | " + board[8])
#
# def check():
#     return (board[0] == board[1] == board[2] == player or
#             board[3] == board[4] == board[5] == player or
#             board[6] == board[7] == board[8] == player or
#             board[0] == board[3] == board[6] == player or
#             board[1] == board[4] == board[7] == player or
#             board[2] == board[5] == board[8] == player or
#             board[0] == board[4] == board[8] == player or
#             board[1] == board[4] == board[6] == player)
#
# while not game_over:
#     show()
#     move = int(input("\nХод " + player + "(1-9):")) - 1 # move то значение которое вводит пользователь
#     if board[move] == " ":
#         board[move] = player # на игровое поле board по индексу move который вводит польз присваиваем
#     else:
#         print("Занято")
#         continue  # чтобы в таком случае не менялся ход игрока
#
#
#     if check():
#         show()
#         print("\nПользователь  " + player + " победил")
#         game_over = True
#     elif " " not in board: # если пустые ячейки не наход в борд
#         show()
#         print("\nНичья")
#         game_over = True
#
#
#     player = "0" if player == "X" else "X"

#=========================================

# a = "Hello"
# b = "Hello"
# print(a == b) # True
# print(a is b) # True две переменные ссылаются на 1 ячейку памяти
# print("id(a)", id(a))
# print("id(b)", id(b))
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2) # True
# print(lt1 is lt2) # False две переменные не ссылаются на одну ячейку памяти
# print("id(lt1)", id(lt1))
# print("id(lt2)", id(lt2))

# lt1 = [1, 2,3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
#
# s = ("Hello")
# print(s, id(s))
# s += " world"
# print(s, id(s))

#=========
# кортеж = tuple (неизменяемый тип данных)
#
# lst = [10, 20 ,30] # список
# tpl = (10, 20, 30) # кортеж
#
# # print(lst[1]) # обратились к элементу списка по индексу
# # print(tpl[1]) # обратились к элементу кортежа по индексу
# print(lst.__sizeof__()) # рaзмер в байтих 72
# print(tpl.__sizeof__())# рaзмер в байтих 56
#
# lst[1] = 5
# print(lst)
# # tpl[1] = 5 # нельзя затереть
# # print(tpl)

# a = 1, 2, 3, 4, 5
# print(a, type(a))

#
# b = tuple("Hello World")
# print(b, type(b))
#
# print(b[1:3])

# s = tuple(int(input("-> ")) for i in range (5))
# print(s)

# s = input("Введите пятизначное число: ")
# tpl = tuple(s)
# print(tpl)
#
# res = 0
# for i in tpl:
#     res += int(i)
# print(len(tpl))
# print(res)
# print(res / len(tpl))

#=================
# import random
#
# tpl = tuple(random.randint(1, 100) for _ in range(10))
# print(tpl)

#=================
# t1 = tuple("hello")
# t2 = tuple("world")
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))

#================= слайсер:
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             print(first)
#             return tpl[first:second]
#
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#     # pass #временная заглушка
#
#
# print(slicer((1,2,3), 8))
# print(slicer((1,8,3,4,8,8,9,2), 8))
# print(slicer((1,2,8,5,1,2,9), 8))

#=================
# tpl = (10, 11, [1,2,3], [4,5,6], ["hello", "world"])
# print(tpl, id(tpl))
# tpl[4][0] = "new"
# print(tpl, id(tpl))
# tpl[4].append("new")
# print(tpl, id(tpl))

#================= распаковка кортежа
# tpl = 1, 2, 3
# # x = tpl[0]
# # y = tpl[1]
# # z = tpl[2]
# x, y , z = tpl # распаковка кортежа
# print(x, y, z)

# def get_user():  #если функция возращает больше 1 элемента - кортеж
#     name = "Tom"
#     age = 20
#     is_married = True
#     return name, age, is_married
#
# user, year, married = get_user()
# print(user, year, married)

# 04.07.2026

# import random
#
#
# def run(a,b):
#     return tuple(random.randint(a,b) for _ in range(10))
#
#
# tpl1 = run(0, 5)
# print(tpl1)
# tpl2 = run(-5, 0)
# print(tpl2)
#
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0= ", tpl3.count("0"))

# a = (0, 3, 5, 2, 1, 0, 0, 5, 5, 1)
# # del a
# b = list(a)
# print(b)
# b[0] = 100
# print(b)
# c = tuple(b)
# print(c)

#======

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries, end="\n\n")
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана: ", countryName, ", население = ", countryPopulation, sep="")
#     for city in cities:
#         cityName, cityPopulation = city
#         print("Город: ", cityName," население= ",cityPopulation, sep="")


#======
# tpl = tuple(input("Введите данные: "))
# print(tpl)
#
# lst = []  # изначально пустой
# for item in tpl:
#     if item not in lst:
#         lst.append(item)
#
# for item in lst:
#     print("Колличество: ", item, "=", tpl.count(item))

#====== множества set хранятся только уникальные значения. Неупорядоченная коллекция
# данных
# s = {'banana', 'apple', 'mango', 'banana', 'apple',}
# print(s, type(s))
# for x in s:
#     print(x)

# a = set("hello")
# print(a, type(a))
#
# s = {x * x for x in range(10)}
# print(s)

# t = {'red', 'green', 'blue'}
# print("green" in t)
# print("yellow" in t)


#======


# t = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = [i for i in t if "a" not in i]
# # a = ["A" + i[1:] if i[0] == "a" else "B"+ i[1:] for i in t]
# a = {"A" + i[1:] if i[0] == "a" else "B"+ i[1:] for i in t if i[1]=='c'} # тернарное выражениее
# print(a)

# a = {0,1,2,3}
# print(a)
# a.add(4)
# print(a)

# users = {"Tom", "Bob", "Alice"}
# print(users)
# # users.remove("Tom")
# # print(users)
# # users.remove("Ann")  #KeyError
# # print(users)
# user = "Ann"
# if user in users:
#     users.remove(user)
# print(users)
# # users.discard("Tom") #удаление. Не выбрасывает исключения
# # print(users)
# # users.pop() # удаляет случайный элемент , кторый был 1 в множесве
# # print(users)
# # users.clear()
# # print(users)
# users.add("Ann")
# print(users)

#========================

# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a.union(b) # объединение множества без дубликатов {0, 1, 2, 3, 4}
# print(c)
# c = a|b # {0, 1, 2, 3, 4}
# # print(c)
# a |= b # {0, 1, 2, 3, 4}
# print(a)

# c = a & b # те элементы котрые встреч 1 и 2 сете(пересечение множест)
# print(c)
# a &= b записываает те элементы котрые встреч 1 и 2 сете(пересечение множест)
# print(a)
#
# c = a - b
# print(c) # {0}
# a -= b # {0}
# print(a)

# c = a ^ b # {0, 4} записывает только уникальные элементы в множествах a и b
# print(c)
# a ^= b # {0, 4}
# print(a)

#========
# s1= {1,2}
# s2= {3}
# s3= {4,5}
# s4= {3,2,6}
# s5= {6}
# s6= {7,8}
# s7= {9,8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 |s3| s4| s5| s6| s7 # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s)
# count  = len(s)
# print("Кол-во элементов: ",count)
# print("min: ",min(s))
# print("max: ",max(s))

#========

# s1 = "Hello"
# s2 = "How are you?"
# s = set(s1) & set(s2)
# print(s)
# s1 = set("Hello")
# s2 = set("How are you?")
# s = s1 & s2
# print(s)
# for i in s:
#     print(i, end=" ")


# Найти ввсе буквы в первой строке, которые отсут во второй
# s1 = "Python"
# s2 = "Programming languages"
# a = list(set(s1) - set(s2))
# print(a)
# for x in a:
#     print(x, end=" ")

# a = {0,1,2,3,4}
# b = {3,2,1}
#
# print (a <= b)
# print (a < b)
# print (a >= b)
# print (a > b)

#========
#
# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
# both_hobbies = drawing & music
# print("Два кружка: ",both_hobbies)
#
# drawing -= both_hobbies
# print(drawing)

#========
# s= frozenset([1,2,3,4,5])
# s = frozenset({"Hello", "World"})
# print(s)


#===============
# 05.07.2026

# lst = [10, 20, 30]
# d = {"one": 1, "two": 20, "three": 30} # словарь или ассоциативный массив.
# # Вместо индекса ключ
# print(lst[0])
# print(d["one"])

# d = {"one": 1, "two": 20, "three": 30} # это не сет, это словарь
# print(d, type(d))
#
# d1 = dict(one=1, two=20,three=30)
# print(d1, type(d1))

# d = {0: "text", "one":45, (5,4):"кортеж", "список":[2,4,5], True:1, False:0, "список":[0,0,0]}#ключ
# # ами могут быть неизменяемые типы данных
# print(d)

# lst = [1,2,3]
# print(tuple(lst))

# lst = (
#     ("one",1),("two",2),("three",3)
# )
# print(dict(lst))

# d = {a ** 3: a ** 2 for a in range(2,10)} # генератор из словаря
# print(d)

# d = {"one": 1, "two": 20, "three": 30}
# print(d)
# print(d["two"])
# d["two"] = 2 ** 4
# print(d)


#
# d = {0: "text", "one":45, (5,4):"кортеж", "список":[2,4,5], True:1, False:0,1:45}
# print(d)

# print("список" in d) #проверка есть ли сам ключ в словаре
# print("списки" in d)#проверка есть ли сам ключ в словаре

# try: # блок try попытется выполнить del, если может, то блок except не отрабат
#     del d["one1"] # удаление по ключу
# except KeyError:
#     print("Элементом с таким ключом не существует")
# print(d)



# print(d[0])
# print(d[True])
# print(d[1])
# print(d[(5,4)])
# print(d["список"][1])


# d = {0: "text", "one":45, (5,4):"кортеж", "список":[2,4,5], True:1, False:0,1:45}
# print(d)
#
# for key in d:
#     print(key,":" ,d[key])

#====================
# созздать словарь и перемножить все значения
# d = {"x1":3, "x2":7, "x3":5 , "x4":-1}
#
# res =1
# for key in d:
#     res *= d[key]
#
# print(res)

#====================
#Предложите пользователю ввести название 4х
# овощей и сохраните их в словаре с числовыми индесами

# длинная запись:
# d = dict()
# d[1]=input("->")
# d[2]=input("->")
# d[3]=input("->")
# d[4]=input("->")

#короткая запись
# d = {i: input("->") for i in range(1,5)} # создали 4 итерации по вводу в словарь. i:(ключ) d(input)
# # значение. Наполнение словаря с клавиатуры
# print(d)
#
# delete = int(input("Какой элемент исключить: "))
# del d[delete] #удаляем предмет по введеннгому пользователем
# print(d)


#====================

# goods = {
#     '1': ["Core-i3-4330", 9, 4500],
#     '2': ["Core-i5-4678", 3, 8500],
#     '3': ["AMD FX-6300", 6, 3700],
#     '4': ["Pentium G3220", 8, 2100],
#     '5': ["Core-i3-3450", 5, 6400]
# }
#
# for i in goods: # в цикле проходимся по коллекции. i - как ключ
#     print(i, ") ",goods[i][0],"-",goods[i][1]," шт. по ", goods[i][2] ,"руб", sep="", )
#
# # редактирование с клавиатуры пользователя:
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods: # если введен существующий ключ, то функция выполняется, если нет в начало
#             while True:
#                 try:
#                     count = int(input("Кол-во: "))
#                     goods[n][1] += count
#                     break #если введено корректное кол-во прерывается вложенный while
#                 except ValueError:
#                     print("Значение некоректное. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for i in goods: # чтобы выводились измененные элементы
#     print(i, ") ",goods[i][0],"-",goods[i][1]," шт. по ", goods[i][2] ,"руб", sep="", )

#====================


# Методы у словарей:

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# print(dir(dict))

# print(d.keys()) #получаем ключи #(['one', 'two', 'three'])
# print(d.values()) #получаем значение ключей (['one', 'two', 'three'])
# print(d.items()) #получаем ключей и значений ([('one', 1), ('two', 2), ('three', 3)])

# for key, value in d.items():
#     print(key, value)

# value =d["two"] # получили доступ к зннчению ключа 2
# value = d.get("two") # получили доступ к значению ключа 2
# value = d.get("four", "Такого ключа нет")
# print(value)

# item = d.pop("three") #возращает само значение удалееннного элемента
# item = d.pop("three", 4) #возращает само значение удалееннного элемента
# print(item)
# print(d)

# item = d.popitem() # удаляет последни ключ и значение
# print(item)
# print(d)

# d.clear() #  словарь полностью очистился
# print(d)
# item = d.setdefault("one") # вернул значениее ключа, не изменив словарь
# print(item)
# print(d)

# item = d.setdefault("four", 4) # вернул значениее ключа, c добавлением в словарь со значенинием
# print(d)


# d1 = dict.fromkeys(["a", "b", "c", "d"], 100)
# print(d1)
#
# d = {"one": 1, "two": 2, "three": 3}
# print(d)
#
# d2 = d.copy() # копия
# print("d", d)
# print("d2", d2)
#
# d["two"] = 5
# d2["three"] = 6
# print("d", d)
# print("d2", d2)

# d = {"a": 1, "b": 2, "c": 3}
# d2 = {"one": 1, "two": 2, "three": 3}
# d.update({"a": 4, "e": 5, "f": 6})
# d.update(d2)
# d.update([("r",7), ("q",9)])
# print(d)


# d = {"a": 1, "b": 2, "c": 3}
# d2 = {"one": 1, "two": 2, "three": 3}
#
# d3 = d|d2
# print(d3)

#=======

# d = {"name": "Kelly", "age":25, "salary": 8000, "city":"New York"}
# print(d)
#
# # new_d = dict()
# # new_d["name"] = d.pop("name") #удааляем знаачение по ключу name.
# # # Само значение записываем в новый словарь с новым ключом
# # new_d["salary"] = d.pop("salary")
#
# new_d = {"name":d.pop("name"), "salary":d.pop("salary")}
#
# print(d)
# print(new_d)


#=================изменить ключ

# d = {"name": "Kelly", "age":25, "salary": 8000, "city":"New York"}
# d["location"] = d.pop("city")
# print(d)

#=================
# d = {
#     "first":{
#         1:"one",
#         2:"two",
#         3:"three"
#     },
#     "second":{
#         4:"four",
#         5:"five"
#     }
# }
# print(d)
#
# # for x in d: #берет только основные ключи first и second
# #     print(x)
# #     for y in d[x]: #по ключу x ьерет вложенные элементы
# #         print("\t",y, ": ", d[x][y], sep="")
#
# for x, y in d.items():
#     print(x)#берет только основные ключи first и second
#     for i, j in y.items():
#         print("\t",i, ": ", j, sep="")

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
#
# new_d = {v:k for k,v in d.items()} #поняли местами ключи и значения
# print(new_d)



#=================дз
# имена - основные ключи словаря
# вложенные ключи:
# запросить имемя, затем регион. и нам должны показать какие продажи сейчас выаести соответ данные.
# запросить

#11.07.2026
# lst = [1,2,3,4]
# d = {k: int(input("->"))for k in lst}
# print(d)

# d = dict(zip([1,2,3], ["one","two","three"]))
# print(d)

# print(list(zip([1,2,3])))

# one = {'name': 'Igor', 'surname': "Vetrov", "age": 26}
# two = {'name': 'Irina', 'surname':"Petrova",'age': 20}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#      print(k1, "->", v1)
#      print(k2, "->", v2)

# one = {"one": 1, "two": 2}
# two = {"three": 3, "four": 4}
# print({**one, **two}) # {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
#
# def func(*args):
#      return args
#
#
# print(func(1,2,3))


# def average(*args):
#      return sum(args) / len(args)
#
#
# print(average(1,2,3,4,5,6))
# print(average(1,2,3))

#==========

# def average(*args):
#      aver = sum(args) / len(args)
#      print(aver)
#      res = []
#      for num in args:-
#           if num < aver:
#                res.append(num)
#      return res
#
#
# print(average(1,2,3,4,5,6,7,8,9))
# print(average(3,6,1,9,5))

#==========


# def func(a, *args):
#      return a, args
#
# print(func(1))
# print(func(1, 2, 3))
#==========

# def print_data(student, *scores):
#      print("Student name: ",student)
#      for score in scores:
#           print(score)
#           print(*scores)
#           print(scores)
#
# print_data("Igor", 100, 95, 88,92,99)
# print_data("Marina", 96, 20,33,56)
# print_data("Irina")

#==========
# def func(**kwargs):
#      return kwargs
#
#
# print(func())
# print(func(a = 1, b=2, c=3))
# print(func(lang ="Phyton"))



# def func(a, b, *args, e = 0,**kwargs):
#      return a, b, args, kwargs, e
#
# print(func(1, 2, 3, 4, 5, 6, c =6, d=7, e=100))
# print(func(1)) # (1, (), {})
# print(func(1, 2,3)) # (1, (), {})
# print(func(1, 2,3, c=4, d=5)) # (1, (), {})


# область видимости переменных(там где переменная видна и там где не видна)
#сущ 4 области видимости:

# name = 'Tom'# глобальная (за пределами функции)
#
# def hi():
#      surname = "Johnson" #локакльная (внутри функции) видимость внутри
#      # функции
#      name = "Sam" #можем перезаписать глоб переменную,
#      # но значение будет видно внутри функции
#      print("Hello ",name, surname)
#
#
# def buy():
#      print("good bye", name)
#
# hi() # локальная
# buy()

#======================

# import builtins
#
# names = dir(builtins)
# for name in names:
#      print(name)

#======================
# one = 10
#
# def func(a):
#      one = 100
#      x = 2 # область объемлющих функций
#
#      def inner():
#           one = 1000
#           # print("x= ", x)
#           return one
#
#      return inner()
# print(func(5))

#======================
#вложенные функции:
#
# def outer(who):
#
#      def inner():
#           print("Hello, ", who) # 3
#      inner() # 2
#
# outer("World") # 1


#======================
# who = "World"
#
#
# def outer():
#      global who #перезаписали глобальноую переменную
#      who = "Mari"
#
#      def inner():
#           print("Hello, ", who)
#      inner()
#
# outer()
# print(who)

#======================
#
# def fn1():
#      x = 25
#
#      def fn2():
#          x = 33
#
#          def fn3():
#               nonlocal x #поднимает на уровень выше
#               x = 55
#               print("fn3.x =", x)
#
#          fn3()
#
#          print("fn2.x =", x)
#
#      fn2()
#      print("fn1.x =", x)
#
# fn1()

#===============
#
# x = 25
# t = 0
#
#
# def fn():
#      global t
#      a = 30 # 35
#
#      print("global: ", x)
#
#      def inner():
#           nonlocal a
#           a = 35
#           print("nonlocal: ", a)
#
#      inner()
#      print(a)
#      t = a
# fn()
#
# c = x + t
# print(c)
#
#

#===============

# def outer (a1, b1, a2, b2):
#      a = 0
#      b = 0
#      def inner():
#           nonlocal a, b
#           a = a1 + a2
#           b = b1 + b2
#
#      inner()
#      return [a, b]
#
# print(outer(2, 3, -1, 4))
#===============

# замыкание:

# def outer(n): # 1   #3
#      def inner(x): # 10  #10
#          return x + n # 11
#
#      return inner
#
# add1 = outer(1)
# print(add1(10))
#
# print(outer(3)(10))

#===============

# def outer():
#      a = 1
#      b = "line"
#      c = [1, 2, 3]
#
#      def inner():
#           nonlocal a, b
#           c.append(4)
#           a = a + 1
#           b = b + " new"
#           return a, b, c
#
#      return inner
#
# func = outer()
# print(func())
# print(func())



# 12.07.2026
# Анонимные функции:\Лямда выражения
# print((lambda x, y: x + y)(1,2))
# print((lambda n, m: n ** 2 + m ** 2)(2,5))


# summ = lambda a = 1, b = 2, c = 3: a + b + c
# print(summ(10, 20, 30))

# print((lambda *args: sum(args))(1,2,3,4))

# tpl = (
#      lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4
# )
#
# for t in tpl:
#      print(t("abc"))

#===
# def outer(n):
#      def inner(x):
#           return x + n
#
#      return inner
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#      return lambda x:x + n
#
# f = outer(42)
# print(f(3))
#
#
#
# outer = lambda n: lambda x:x + n
#
# f = outer(42)
# print(f(3))
#
# print((lambda n: lambda x: x + n)(42)(3))

#===
# d = {"b": 15, "c": 5 , "a": 10}
# lst = list(d.items()) # преобразовали к списку кортежей
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

#===

# lst = [
#      lambda x, y: x + y,
#      lambda x, y: x - y,
#      lambda x, y: x * y,
#      lambda x, y: x / y
#           ]
#
# print(lst[0](5,12))
# print(lst[1](12,5))

#===
# d = {
#      1:lambda: print("Понедельник"),
#      2:lambda: print("Вторник"),
#      3:lambda: print("Среда"),
#      4:lambda: print("Четверг"),
#      5:lambda: print("Пятница"),
#      6:lambda: print("Суббота"),
#      7:lambda: print("Воскресенье")
# }
#
# d[3]()


#===
# print((lambda a, b: a if a > b else b)(15, 13))
# print((lambda a, b, c : min(a, b, c))(9, 8, 5))

#===Циклы: 1:03
# map(function, *iterables)

# def mult(t):
#     return t * 2
#
# lst = [2, 8 ,12, -5, -10]
#
# print(list(map(mult, lst)))
# print(list(map(lambda t : t * 2,lst)))

# old = ['5', '4','7','8']
# print(old)
# print(list(map(int, old)))

#
# st = ["a", "b", "c", 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x,y: (x, y), st, num)))
# print(dict(map(lambda x,y: (x, y), st, num)))

# t = ('abcd', 'abc', 'cdefq', 'def', 'teo')
# print(tuple(filter(lambda s: len(s) == 3, t)))

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 0]
# print(list(filter(lambda s: s > 75, lst)))
# print(list(filter(lambda s: s, lst)))
# print(list(filter(lambda s: s + 2, lst)))

# декораторы:
# функция которая принимает другую функцию
# def hello():
#     return "Hello, I am func, 'hello'"
# def supper_func(func):
#     print("Hello, I am supper func")
#     print(func())
#
# supper_func(hello)


# def hello():
#     return "Hello, I am func, 'hello'"
#
# tes  = hello
# print(tes())

# def my_decorator(func):
#     def wrapper():
#         print("code before")
#         func()
#         print("code after")
#     return wrapper
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()



# def my_decorator(func):
#     def wrapper():
#         print("code before")
#         func()
#         print("code after")
#     return wrapper
# @my_decorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


# def circle(fn):
#     def wrap():
#         return "(" + fn() + ")"
#     return wrap
#
# def angle(fn):
#     def wrap():
#         return "<" + fn() + ">"
#     return wrap
#
# @angle
# @circle
# def expression():
#     return "5 + 2"
#
#
# print(expression())

# def cnt(fn):
#     count = 0
#
#     def wrapper():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrapper
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(func):
#     def wrap(arc1, arc2):
#         func(arc1, arc2)
#         print("Данные: ", arc1, arc2)
#
#     return wrap
#
# @args_decorator
# def full_name(name, surname):
#     print("Меня зовут",name, surname)
#
# full_name("Ирина", "Ветрова")


# def args_decorator(func):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         func(*args, **kwargs)
#
#
#     return wrap
#
# @args_decorator
# def full_name(a,b,c, study = 'Phyton' ):
#     print(a, b, c,"изучают", study, end="\n\n")
#
# full_name("Ирина", "Борис", 'Светлана', study='JavaScript' )
# full_name("Владимир", "Екатерина", 'Виктор' )


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(a, b):
#             print(args1 , a, args2, b, '=', end=' ')
#             return fn(a, b)
#
#         return wrap
#     return args_dec
#
# @decor("Сумма", '+')
# def summa(x, y):
#     print(x + y)
#
# @decor("Разность",'-')
# def sub(x, y):
#     print(x-y)
#
# summa(5, 2)
# sub(5, 2)



# def multiply(arg): # 3
#     def decor(func): # return_num
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5)) #5

# def avg(fn):
#     def wrap(*args):
#         print ('Среднее арифмитеческое: ', args, '=', fn(*args) / len(args))
#         return fn(*args)
#
#     return wrap
#
# @avg
# def summa(*args):
#     print('Сумма чисел: ', args, '=', sum(args))
#     return sum(args)
#
# summa(2,3,3,4)


#18.07.2026
#
# print (bin(18)) # 0b10010
# print (oct(18)) # 0o22
# print (hex(18)) # 0x12
#
#
# print (0b10010) # 18
# print (0o22) # 18
# print (0x12) # 18
#
#
# print (0b10010 + 0o22 + 0x12 + 18) # 72
#
#
# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print('y' in e)
#
# # print(e[1])
# # print(e[1:5])
# # print(e[1:5:2])
# # print(e[10:20])
# print(e[::-1])

#у каждого символа есть кодд символа

# print("Привет")
# print(u"Привет")
# print(r"C:\folder\file.py")
# print("C:\\folder\\file.py")

# name = 'Дмитрий'
# age = 25
#
# print('Меня зовут ', name, ". Мне ", age, ' лет', sep='')
# print('Меня зовут '+ name + ". Мне " + str(age) + ' лет')
# print(f"Меня зовут {name}. Мне {age} лет")

# x = 10
# y = 5
# print(f"{x} * {y} / 2 = {x * y / 2}")
# print(f"{x=}, {y=} ")
# print(x, y)

# mas = [4, 5, 7,8]
# print(f'{mas[1]}')

# print(f"13/3 = {round(13/3,2)}")
# print(f"13/3 = {13/3:.2f}")

# dir_name = "folder"
# file_name = "file"
# print(fr"home\{dir_name}\{file_name}")

# a = ("hello "
#      "world")
# print(a)
#
# b = """hello
# world"""
# print(b)
#
# c = ''''Hello
# World'''
# print(c)

# def square(x):
#     """"Принимает число n, возращает квадрат числа n"""
#     b = 4
#     return x ** 2
#
#
# print(square(3))
# print(square.__doc__)
# # print(max.__doc__)
# print(len.__doc__)

# import math
# def cylinder(r,h):
#     """
#     Вычисляет площадь циллиндра.
#
#     Вычисляет площадь циллиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
# print(cylinder(2,4))
# print(cylinder.__doc__)

# print(ord('a')) # 97
# print(ord('ю')) # 1102

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# my_str = "Test string for me "
# arr = [ord(x) for x in my_str] #прошлись по каждой букве
# print("ASCII коды", arr)
#
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
#
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1])-1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))

#генерация пароля:
# from random import randint
#
# shortest = 6
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_lengt = randint(shortest, longest)
#     res = ""
#     for i in range(random_lengt):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:",random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize()) # Hello, world! i am learning python.
# print(s.lower()) # hello, world! i am learning python.
# print(s.upper())# HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())# HELLO, world! i AM LEARNING pYTHON.
# print(s.title())#Hello, World! I Am Learning Python.

# print(s.count("l", 3, 10))
# # print(s.lower().count("l")) # hello, world! i am learning python.
# # Потом ищем букву l

# print(s.find("l")) #
# print(s.rfind("l"))  # поиск справа
#
# print(s.index("l"))
# print(s.rindex("l")) # поиск справа

#
# print(s.endswith("on"))
# print(s.startswith("WORLD", 7))

# print("abc123".isalnum()) # True проверяет наличие в строке и цифры и буквы
# print("abc123!".isalnum()) # False спец символы

# print("abc123".isalpha()) # False проверка что тут только буквы
# print("123".isdigit()) #проверка что тут только цифры


# print("abc@".islower())# True проверка все в нижнем регистре
# print("abcA".islower())# False
# print("abcA".isupper())# False проверка элементов на верхний реггистр

# print("py".center(10, "-"))

# print("    py".lstrip())
# print("py  ".rstrip())
# print("   p y  ".strip())


# print("https://wwww.python.org/".strip("/:pths").rstrip("/org"))

# s = "Я изучаю Nython. Мн нравится Nython. Nython очень интересный язык программирования"
# print(s.replace("Nython", "Python", 2))

# s = "-"
# seq = ("a", "b", "c", "d")
# print(s.join(seq)) #превращает символы в строку и каждый элементы разделены -
#
# print("..".join(['1','2'])) # 1..2
#
# print("..".join("Hello")) # H..e..l..l..o


# print("Строка разделенная пробелами".split())
# print("www.python.org".split("."))

# a = input("->").split()
# print(a)


# def fio(name):
#     print(f"{name[0]} {name[1][0]}.{name[2][0]}.")
#
# st = input("Введите ФИО: ").split()  # Никонов Валерий Анатольевич
# print(st)
#
# fio(st)


#==============================================================
#19.07.2026
#работа с файлами:

# f = open("text.txt","r")
# f = open("C:\\Users\\Дмитрий\\Desktop\\AD622\\text.txt","r")
# f = open(r"C:\Users\\Дмитрий\Desktop\AD622\text.txt","r")
# print(f)
# print(*f)
# print(f.mode) #
# print(f.name)
# print(f.encoding)
# print(f.closed)  #проверка открыт или закрыт файл

#
#
# f = open("text.txt")
# print(f.read(3)) #прочитать файл (3) сколько символов
# print(f.read()) # второй вызов дочитает
# f.close() # подверждение сохранения данных


# f = open("text.txt")
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open("test.txt")
# print(f.readline()) # считали строку документа
# print(f.readline(8)) # считали строку документа конкретно 8 символов
# print(f.readline()) # считали остатки строки
# print(f.readline()) # считали какую то строку
# print(f.readline()) # считали какую то строку
# f.close() # подверждение сохранения данных

# f = open("test.txt")
# print(f.readlines(16)) #Если захватили элемент с новой строки, то выводится она полностью
# print(f.readlines())
# f.close() # подверждение сохранения данных

# f = open("test.txt")
# for line in f:
#     print(line)
#
# f.close()


# f = open("xyz.txt", "w")
# f.write("Hello \nWorld!\n")
# f.close()

#
# f = open("xyz.txt", "a") # режим "a" запсывает в существующий файл
# f.write("New text.\n")
# f.close()


# f = open("xyz.txt", "w") # существующий фалй режим "w" очищает
#
# f.close()


# f = open("xyz1.txt", "a") #
#
# f.close()
#===================================
# r - режим чтения (файл должен быть создан!)
# w - режим записи,  файла может не быть. Если файл создан, то все сотрет
# a - режим дозаписи в существующий файл,  файла может не быть(создаться чистый)
#===================================

# f = open("xyz.txt", "w") #
# lines = ["Thus is line 1\n", "Thus is line 2\n"]
# f.writelines(lines)
# f.close()


#
# lines = [str(i) + "\t" for i in range(1,20)]
# print(lines)
# f = open("xyz.txt", "w") #открыли и очистили что было перед этим
#
# f.writelines(lines) # работает толькоо со строковыми значениями
# f.close()

#================
#
# f = open("text2.txt","w") # открыли в режими записи и создали новый
# f.write("Замена строки в тектсовом файле;\nизменить строку в списке;"
#         "\nзаписать список в файл;\n")
# f.close()
#
# #открыли и считали данные
# f = open("text2.txt","r")
# read = f.readlines() # считали строку
# f.close()
#
# # изменили данные
# print(read)
# read[1] = "hello world!\n"
# print(read)
# f.close()
#
#
# # перезаписали данные с новым содержимым
# f = open("text2.txt","w")
# f.writelines(read)
# f.close()
#================

# f = open("text.txt","r")
# print(f.read(3))
# print(f.tell()) # 3 показывает на какой позиции где он находимся когда мы ууже что то считали
# print(f.seek(1)) # 1 на какую позицию мы переносим курсор
# print(f.read()) # ello! считет оттуда где курсор
# print(f.tell()) #6 показывает на какой позиции где он находимся когда мы ууже что то считали
# f.close()
#
# f = open("text.txt","w")
# print(f.write("I am leaning Python"))
# print(f.seek(3))
# print(f.write("- new string-"))
# print(f.tell())
# f.close()

# 1;09
# f = open("text223.txt","a+")
# f.write("Hello \nWorld\n")
# print(f.readlines())
# f.close()

# with open("text.txt", "w") as f: # контексный менеджер, сам закрывает файлы
#     print(f.write("0123456789"))
# print(f.closed) # показывает что за пределами файл закрыт


# with open("text2.txt", "r") as f:
#     for line in f:
#         print(line[:3])

# file_name = "test.txt"
# lst = [4.5, 2.8, 1.0, 0.3, 4.3, 7.777]
# def get_line(lt):
#     lt = map(str, lt) # lt = [] берет по очереди
#     # каждый элемент списка и применяет str
#     # ["4.5", '2.8', '1.0', '0.3', '4.3', '7.777']
#     return " ".join(lt) # каждый элемент будет объединен
#     # в одну строку и разделен вместо запятой пробельным символом
#     # "4.5 2.8 1.0 0.3 4.3 7.777"
#
#
# with open(file_name, "w") as f:
#     f.write(get_line(lst)) #записывает строку 4.5 2.8 1.0 0.3 4.3 7.777
#
# print("Done!")
#
#
# with open(file_name, "r") as f:
#     nums = f.read()
#
# print(nums)
#
# num_list = list(map(float, nums.split())) #из строки разобьет элементы а список
# print(num_list)
# print(sum(num_list))

#================

# def longest_words(file):
#     with open(file, encoding="utf-8") as f:
#         w = f.read().split() # из строки получили данные в виде списка
#         print(w)
#         max_length = len(max(w, key=len)) # сортировка по длине и
#         # наодим самое длинное слово
#         res  = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("text.txt"))


#================
# text = ("Строка №1\nСтрока №2\nСтрока №3"
#         "\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7"
#         "\nСтрока №8\nСтрока №9\nСтрока №10")
#
# with open("one.txt", "w") as f:
#     f.write(text)

# read_file = "one.txt"
# write_file = "two.txt"
#
# with open(read_file, "r") as fr, open(write_file, "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


#Json
#Сериализация и десериализация

#dump() - сохраняет данные в открытый файл
#load - считывает данные из открытытого файла#
#dupms - сохраняет данные в строку
#loads - считывает данные из строки

#
# import pickle
#
# file_name = "basket.txt"
#
# shop_list = {"фрукты": ["Яблоки", "Манго"],
#              "овощи": ("Морковь","Лук" ),
#              "бюджет": 1000}
#
# # with open(file_name, "wb") as f:
# #     pickle.dump(shop_list, f)
# #
# # with open(file_name, "rb") as f:
# #     print(pickle.load(f))
#
# shop = pickle.dumps(shop_list)
# print(shop)
#
# load_shop = pickle.loads(shop)
# print(load_shop)
#
#
# import json
#
# data = {
#     'name': "Olga",
#     'age': 20,
#     20: None,
#     True: True,
#     False: False,
#     "list": (5,8,9,7)
# }
#
# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4)

#============
# 01.08.2026

# import sqlite3


# conn = sqlite3.connect('profile.db') # устанавливает соединение с БД
# cur = conn.cursor()# служебный метод на каком этапе мы находимся
#
# conn.close()

# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute('''CREATE TABLE IF NOT EXISTS users (
#     #     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #     name TEXT NOT NULL,
#     #     summa REAL,
#     #     date BLOB
#     # )''')
#     cur.execute("DROP TABLE IF EXISTS users") #удалить таблицу если существует



# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS person (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     phone BLOB DEFAULT "+7999000000",
    #     age INTEGER NOT NULL CHECK (age >= 0 AND age <= 100),
    #     email TEXT UNIQUE NOT NULL
    #     )
    # ''')
    # cur.execute('''ALTER TABLE person
    #  RENAME TO person_table
    #  ''')
    # cur.execute('''
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT
    #  ''')
    # cur.execute('''
    # ALTER TABLE person_table
    # ADD COLUMN SURNAME TEXT  NOT NULL DEFAULT "fio"
    #  ''')
    # cur.execute('''
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address
    #  ''')
    # cur.execute('''
    #    DROP TABLE person_table
    #     ''')
# 22.08(повтор)
# import sqlite3
#
# # conn = sqlite3.connect('profile1.db') #  метод connect
# # # устанавливает соедиенение с БД.
# # # ЕСЛИ БД не существует, он ее создаст
# # cur = conn.cursor() #  cur слежебный
# # # элемент понимает на каком этапе он находится
# #
# # conn.close() # закрываем
#
# with sqlite3.connect('profile1.db') as con: # в таком случае клоуз не нужен за счет with
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         summa REAL,
#         date BLOB
#     )''')
#     cur.execute("DROP TABLE IF EXISTS users") #удалить таблицу если существует

#   CREATE TABLE - создать таблицу(команда пишется
#   в верхнем регистре) далее название - users
#   id - уникальное наименование столбцов (ключ)
#   INTEGER - тип данных столбца
#   PRIMARY KEY - показывает, что это первычный ключ
#   AUTOINCREMENT - добавляем +1 1,2,3,4,5,6.....
#   name - наименование столбца NOT NULL - обязательно для заполненение(= не пусто)
#   IF NOT EXISTS - создать таблицу только, если она не существует
#   DROP TABLE IF EXISTS users -удалить таблице если она существует

# 23.08(повтор)
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS person (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         phone BLOB DEFAULT "+7999000000",
#         age INTEGER NOT NULL CHECK (age >= 0 AND age <= 100),
#         email TEXT UNIQUE NOT NULL
#         )
#     ''')

# import sqlite3
#
# with sqlite3.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         ORDER BY FName
#         LIMIT 2, 5;
#     """)
#     res = cur.fetchall() #СЧИТАЕТ ВСЕ ЗАПИСИ
#     print(res)
#
#     res1 = cur.fetchone() # получаем одну запись
#     print(res1)
#
#     res3 = cur.fetchmany(2)
#     print(res3)


    # for res in cur:
    #     print(res)

#Создание БД:
# import sqlite3
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS companies (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER,
#         company_id INTEGER DEFAULT 1,
#         FOREIGN KEY (company_id) REFERENCES companies (id) ON DELETE SET DEFAULT
#     )''')

# import sqlite3
#
# with sqlite3.connect('book.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         count_page INTEGER NOT NULL CHECK (count_page > 0),
#         price REAL CHECK (price > 0)
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS author(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER CHECK (age > 16)
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS author_books(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         books_id INTEGER NOT NULL,
#         author_id INTEGER NOT NULL,
#         FOREIGN KEY (books_id) REFERENCES books(id),
#         FOREIGN KEY (author_id) REFERENCES author(id)
#     )''')
#
# import sqlite3
#
# with sqlite3.connect('study.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS student (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         patronymic TEXT,
#         age INTEGER,
#         "group" INTEGER NOT NULL,
#         FOREIGN KEY ('group') REFERENCES groups(id)
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS groups (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name TEXT
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS association(
#         lesson_id INTEGER NOT NULL,
#         group_id INTEGER NOT NULL,
#         FOREIGN KEY (lesson_id) REFERENCES lessons(id)
#         FOREIGN KEY (group_id) REFERENCES groups(id)
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS lessons(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title INTEGER
#     )''')
#
# import sqlite3

# auto = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 2900),
#     ('Honda', 33000)
# ]
# with sqlite3.connect('cars.db') as con: # (контекстный менеджер with )устанавливаем соединение с БД
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )''')

#     # cur.execute("INSERT INTO cars VALUES (1,'Renault', 22000)")
#     # cur.execute("INSERT INTO cars VALUES (2,'Volvo', 29000)")
#     # cur.execute("INSERT INTO cars VALUES (3,'Mercedes', 5700)")
#     # cur.execute("INSERT INTO cars VALUES (4,'Bentley', 35000)")
#     # cur.execute("INSERT INTO cars VALUES (5,'Audi', 52000)")
#
#     cur.executescript(''' #метод добавления/удаления/ обновления
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     ''')

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES (NULL, ?,?)", auto) # добавление записей через executemany

    # for car in auto:
    #     cur.execute('''INSERT INTO cars VALUES (NULL, ?,?)''', car) добавление строк через цикл

#______________вместо контекстного менеджера with:
# con.commit- схранение данных
# con.clouse() - соединение с БД

# con = None
# try:
#     con = sqlite3.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES (NULL,'Renault', 22000);
#         UPDATE cars SET price = price + 100;
#         ''')
#     con.commit()
#
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()
#____________________
# import sqlite3
#
#
# with sqlite3.connect('cars.db') as con: # (контекстный менеджер with )устанавливаем соединение с БД
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#     name TEXT, tr_in INTEGER, buy INTEGER
#     )''')
#
#     cur.execute("INSERT INTO cars VALUES (NULL,'Запорожец',1000)")
#     last_id = cur.lastrowid # сохраняем посленее число
#     by_car_id = 2
#     cur.execute('INSERT INTO cost VALUES("Федор", ?, ?)', (last_id, by_car_id))
#____________________
# import sqlite3
#
# with sqlite3.connect('cars.db') as con: # (контекстный менеджер with )устанавливаем соединение с БД
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#     name TEXT, tr_in INTEGER, buy INTEGER
#     )''')
#     cur.execute("SELECT model, price FROM cars")
#
# #Вывод данных из БД на консоль:
#     for row in cur:
#         print(row[1])

    # row = cur.fetchone() # возращает в виде кортежа(без списка) из 1 записи
    # print(row)
    #
    # print(cur.fetchmany(5)) # возращает списки кортежей сколько указано в ()
    #
    # print(cur.fetchall())# возращает списки кортежей абсолютно все
#____________________ 05.09 вывод на консоль
# import sqlite3
#
# with sqlite3.connect('cars.db') as con: # (контекстный менеджер with )устанавливаем соединение с БД
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#     name TEXT, tr_in INTEGER, buy INTEGER
#     )''')
#     cur.execute("SELECT model, price FROM cars")
#
# #вывод данных по ключам:
#     for row in cur:
#         print(row['model'], row['price'])


#____________________ изображния
# import sqlite3
#
# def read_ava(n): #читаем через функцию изображение
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# def write_ava(name, data):  #добавляем из бд через функцию изображение
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#         return True
#     except IOError as e:
#         print(e)
#         return False
#
# with sqlite3.connect('cars.db') as con: # (контекстный менеджер with )устанавливаем соединение с БД
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript('''CREATE TABLE IF NOT EXISTS users (
#        name TEXT,
#        ava BLOB,
#        score INTEGER
#     )''')
#
#     # img = read_ava(1) #этот кусок для читаем через функцию изображение
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Федор',?, 1000)",(binary,))
#
#     cur.execute("SELECT ava FROM users LIMIT 1") # для добавляем из бд через функцию изображение
#     img = cur.fetchone()['ava']
#     write_ava('out.png', img) #вызыааем функцию

# import sqlite3
#
# with sqlite3.connect('cars_new.db') as con:
#     cur = con.cursor()
#
#     # with open('sql_dump.sql', 'w') as f:
#     #     for sql in con.iterdump(): # восстанавливаем текущую базу данных
#     #        f.write(sql)
#     with open('sql_dump.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)

# print('изменения после коммита')

# print('Hello world')
# print('Вносим изменения на другом рабочем месте для того же репозитория')
print('Рабочий процесс')