# print("hello world")
# print("Привет мир")
# name = "admin"
# import doctest
# from _pyrepl import keymap
# from doctest import script_from_examples
# from operator import truediv
# from pickletools import read_stringnl_noescape
# from queue import PriorityQueue
# from multiprocessing.reduction import duplicate
# from sqlite3 import dump
# from tarfile import data_filter

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
# print('Рабочий процесс')

# lst = [5,2, [3,4]]
# print(lst)


#====================================================================
# импортировали NumPy
# import numpy as np # для обращения к NumPy дали псевдоним np
# from numpy import dtypes

# 1 вариант:
# lst = [1, 2, 3, 4, 5]
# arr = np.array(lst)
# print(arr)

# lst = [1, 2, 3, 4, 5]
# print(lst * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# 2 вариант:
# arr = np.array([1, 2, 3, 4, 5]) # через метод array создали массив NumPy из списка
# print(arr)
# # print(arr * 2) # [ 2  4  6  8 10]
# #-------
#
# arr2 = np.array([[1, 2, 3, 11, 12, 13], [4, 5, 6, 14, 15, 16]]) # многомерный(двумерный) массив (выводится на разных строках)
# print(arr2) #[[1 2 3]
#             [4 5 6]]

# print(arr2 * 2 ) #[[ 2  4  6] умножение на 2
# #                 [ 8 10 12]]

# кол-во измерений массива:
# print(arr.ndim)
# print(arr2.ndim)

# кол-во строк и столбоцов
# print(arr.shape)
# print(arr2.shape) #

# Общее кол-во элементов:
# print(arr.size)
# print(arr2.size)
# print(len(arr2))

# Обращаемся к элементу:
# print(arr[3])
# print(arr2[0][2])

# print(arr2[0, 2])
# print(arr2[0, :])
# print(arr2[:, 0])  # взяли все данные из нулевого столбца

# print(arr2[0,1:4:2]) # начиная с 1 индекса по 4 не включая его, берем каждое втрое число
# print(arr2[1,0:-1:2])

# arr2[0,0] = 50
# print(arr2)

# arr2[0, :] = [0,0,0,1,1,1]

# zeros = np.zeros((3, 4), dtype='int32') # заполнили нулями
# print(zeros)
#
# ones = np.ones((2,3)) # заполнили единицами
# print(ones)


# создать одномерный массив на 5 нулей
# второй массив 3х4 (3 строчкии 4 значения в них из единиц):
# import numpy as np # для обращения к NumPy дали псевдоним np

# zeros1 = np.zeros((5), dtype='int32')
# print(zeros1)
# ones1 = np.ones((3,4), dtype='int32')
# print(ones1)
#
# mas = np.full((2,3), 5)
# print(mas)

# d = np.random.rand(3,2)
# d = np.random.randint(-5,10, size=(3,4)) # рандом от -5 до 10
# print(d)

# d = np.linspace(0,10,5)
# print(d)

# d = np.arange(0,10,3) # от нуля до 10 не включая 10 с шагом 3
# print(d)

# arr = np.arange(1 , 13) # массив от 1 до 13не включая 13
# print(arr)
#
# two = np.reshape(arr,(3,4))
# print(two)

#создание массивов:
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
#
# hstack = np.hstack((arr1,arr2)) # объединили массивы в строку
# print(hstack)
#
# vstack = np.vstack((arr1,arr2)) # объединили массивы в столбцах
# print(vstack)

# arr1 = np.array([1,2,3, 4])
# print(arr1)
# print(arr1 +3)
# print(arr1 - 2)
# print(arr1 * 2)
# print(arr1 ** 2)

# a = np.array([[1,2],[3, 4]])
# b = np.array([[2,2],[2, 2]])
#
# print(a + b) # кол-во элементов массива
# # должно совпадать для математических операций
# print(a * b)
# print(a ** b)

# a = np.array([[1,2,3],[4,5,6]])
# print(a)

# total = a.sum() # сумма всех элементов массива
# print(total)
#
# col = a.sum(axis=0) # суммирует массивы по индексам
# print(col)
#
#
# row = a.sum(axis=1) # сумма в пределах строки(1 массива)
# print(row)

# mean_all = a.mean() # среднее ариф. всех элементов массива
# print(mean_all)
#
# mean_0 = a.mean(axis=0) #  находит ср. ариф. по индексам(столбцам)
# print(mean_0)
#
# mean_1= a.mean(axis=1) #  находит ср. ариф. по строке
# print(mean_1)

# min_all = a.min() # нашли минимальное значение
# print(min_all)
#
# min_0 = a.min(axis=0) # нашли минимальное значение по столбцам
# print(min_0)
#
# min_1 = a.min(axis=1) # нашли минимальное значение в пределах []
# print(min_1)
#
# max_1 = a.max(axis=1) # нашли минимальное значение в пределах []
# print(max_1)

# arg_max = a.argmax()# индекс максимального числа
# print(arg_max)
#
# arg_0 = a.argmax(axis=0)
# print(arg_0)
#
# arg_1 = a.argmax(axis=1)
# print(arg_1)

# prod_all = a.prod()
# print(prod_all)
#
# prod_0 = a.prod(axis = 0)
# print(prod_0)
#
# prod_1 = a.prod(axis = 1)
# print(prod_1)

# a = np.array([5, 35, 10, 40, 10])
# a = np.array([18, 20, 22, 20, 20])

# var_all = a.var()
# print(var_all)
#
# var_0 = a.var(axis =0)
# print(var_0)
#
# var_1 = a.var(axis =1)
# print(var_1) # дисперсия

# arr1 = np.array([[30,40,35,500, 45, 32,38, 50]])
# print(arr1)
# print(np.median(arr1)) # медиана

# arr = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
# arr = np.array([2, 4, 4, 4, 6])
# print(arr)
# print(np.std(arr))

#СДЕЛАТЬ АНАЛИЗ ДАННЫХ ПО ЗП СОТРУДНИКОВ:
# salaries = np.array([50, 23, 60, 26, 19, 43, 26, 64, 60, 45, 26, 57, 54 ])
# print(salaries)
#
# mean_salary = np.mean(salaries)
# print(f'Средняя зарплата: {mean_salary:.2f}')
#
# max_salary = np.max(salaries)
# min_salary = np.min(salaries)
# print(f'Максимальная зарплата: {max_salary}')
# print(f'Минимальная зарплата: {min_salary}')
#
# std_salary = np.std(salaries)
# print(f'Стандартное отклонение зарплаты: {std_salary:.2f}')
#
# above_mean = salaries[salaries > mean_salary]
# print(f'Зарплата выше среднего: {above_mean}')

#======================================================
# product_ids = np.array([101,102,103,104,105,106,107,108,109,110])
# prices = np.array([10.99, 20.99, 15.49, 25.49, 5.99, 12.99, 7.99, 30.99, 18.99, 9.99])
# quantities = np.array([100, 50, 75, 30, 200,120, 150, 20, 80, 110])
# dates = np.array(['2026-07-01', '2026-07-02', '2026-07-03', '2026-07-04', '2026-07-05', '2026-07-06', '2026-07-07',
#                   '2026-07-08', '2026-07-09', '2026-07-10'])
# #Расчет общих продаж
# total_sales = prices * quantities
# print(f'Общий объем продаж: {total_sales}')
#
# total_sum = np.sum(total_sales)
# print(f'Сумма выручки:{total_sum}')
#
# average_check = np.mean(total_sales)
# print(f'Средний чек:{average_check}')
#
# best_product_index = np.argmax(total_sales)
# wors_product_index = np.argmin(total_sales)
#
# print(f'Лучший товар (ID: {product_ids[best_product_index]}, '
#       f'объем продаж {total_sales[best_product_index]}) ')
#
# print(f'Худший товар (ID: {product_ids[wors_product_index]}, '
#       f'объем продаж {total_sales[wors_product_index]}) ')
#======================================================

#=======================================================

# import pandas as pd

# # series1 = pd.Series([10,20,30,40,50])
# series1 = pd.Series((10,20,30,40,50))
# print(series1)
#
# series2 = pd.Series({'b': 10,'a': 30, 'c':20})
# print(series2)

# series3 = pd.Series(15)
# series3 = pd.Series(15, [3,8,4])
# print(series3)
#
# age = [36,16,23]
# names = ['Сергей', 'Роман', 'Вадим']
# # series4 = pd.Series(age, index = names, name = 'age')
# series4 = pd.Series(age, index = names)
# series4.name = 'age'
# print(series4)
# # print(series4[['Роман', 'Вадим']])
# print('размер серии:', len(series4))
# print('размер серии: ', series4.size)

# series = pd.Series([5, 3, 5, 4, 2, 3, 2, 2])
#
# unique_values = series.unique()
# print('Уникальные значения', unique_values)
#
# value_counts = series.value_counts()
# print('Количество значений в серии')
# print(value_counts)

# age = [36,16,23,29]
# names = ['Сергей', 'Роман', 'Вадим', 'Виталий']
# series = pd.Series(age, index = names)
# print(series)
#
# elem = series.iloc[2] # чтобы получить доступ к элементу метки
# print('\nОдин элемент по позиции: ', elem)
#
# subset = series.iloc[[0,2]]
# print('\nНесколько элементов по позиции: ', elem)
# print(subset)
#
# series = pd.Series([10,20,30,40,50, 60, 70, 80, 90, 100])
# print(series)

# print('Первые пять элемента: ')
# print(series.head(5))
#
# print('Первые три элемента: ')
# print(series.head(3))
#
# print('Последние пять элементов: ')
# print(series.tail())
#
# print('Последние три элемента: ')
# print(series.tail(3))

# sample_data = series.sample(3) # случайные значения
# print(sample_data)

# grades = pd.Series([90,66,86,85,70], index=['Анна','Борис','Влад','Дарья','Елена'])
# print(grades)
#
# # print(grades.nlargest(2, keep='first')) #выводит топ
# # print(grades.nlargest(2, keep='last')) #выводит топ повторяющего последнего элемента
# # print(grades.nlargest(2, keep='all')) #выводит топ повторяющего последнего элемента
#
# print(grades.nsmallest(3, 'first')) # 3 самых низших оценки
# print(grades.nsmallest(3, 'last'))
# print(grades.nsmallest(3, 'all'))

# import numpy as np
# 1. Создайте массив чисел от 10 до 50 с шагом 5:
# d = np.arange(10,50,5) # от нуля до 10 не включая 10 с шагом 3
# print(d)
# 
# 2. Случайные числа: Создайте матрицу размером 3x4 со случайными целыми числами от 0 до 10.
# Выведите ее форму (shape), размер (size) и тип данных (dtype)
# matrix = np.random.randint(0, 11, size=(3, 4))
# print(matrix)
# print(matrix.shape)
# print(matrix.size)
# print(matrix.dtype)
#
# 3. Создайте двумерный массив 4х4. В первой строке заменить все элементы на нули
# arr = np.arange(1, 17).reshape(4, 4)
# # print(arr)
# arr[0,:]=0
# print(arr)
#
# 4. Создайте матрицу 3х3. Найдите сумму
# всех элементов , а также среднее арифметическое отдельно по кадой строке и по каждому столбцу
# arr = np.arange(4, 13).reshape(3, 3)
# print(arr)
# total = arr.sum() # сумма всех элементов
# print(total)
# mean_0 = arr.mean(axis=0) #  находит ср. ариф. по индексам(столбцам)
# print(mean_0)
#
# mean_1= arr.mean(axis=1) #  находит ср. ариф. по строке
# print(mean_1)
#
# 5.массив [8500, 12000, 4300, 9100,11500,15000,6000] в котором записано \
# кол-во шагов за неделю(7 дней). найдите минимальное кол-во шагов, максимальное,
# сумма всех шагов.
# arr = np.array([8500, 12000, 4300, 9100, 11500, 15000, 6000]) # через метод array создали массив NumPy из списка
# print(arr)
# sum_all = arr.sum() # сумма всех шагов
# print(sum_all)
# min_all = arr.min() # нашли минимальное значение
# print(min_all)
# max_all = arr.max() # нашли максимальное значение
# print(max_all)
#
# 6.массив [18.2, 19.5, 21.0, 17.8, 16.5, 23.1, 24.5, 20.0, 19.1, 18.0, 22.4, 25.0, 15.8, 17.2] -
# ежедневная температура в городе за 14 дней.
# найдите среднюю температуру, медиану, стандартное отклонение и дисперсию
# temp = np.array([18.2, 19.5, 21.0, 17.8, 16.5, 23.1, 24.5, 20.0, 19.1, 18.0, 22.4, 25.0, 15.8, 17.2])
# average_temp = temp.mean() # средняя
# print(f'Средняя температура: {average_temp:.2f}')
# print(f'Медиана: {np.median(temp):.2f}')
# std_temp = np.std(temp) # стандартное отклонение
# print(f'Стандартное отклонение зарплаты: {std_temp:.2f}')
# var_temp = temp.var()
# print(f'Дисперсия: {var_temp:.2f}')
#
# 7. Медиана против Среднего
# В небольшом отделе из 5 человек зп составляют: 30, 35, 40, 45, 300 тыс рублей (директор)
# Посчитайте среднюю зарплату и медиану. Посмотрите какой показатель
# лучше отражает реальную ситуацию сотрудников
# salary = np.array([30000, 35000, 40000, 45000, 300000])
# average_salary = np.mean(salary)
# print(f'Средняя зарплата: {average_salary:.2f}')
# print(f'Медиана: {np.median(salary):.2f}') # данный показатель лучше отображает ситуацию
# сотрудников
#
# 8. Индексы экстремумов
# Дана цена на акцию за 5 дней [150, 142, 165, 139, 155].
# найдите номер дня (индекс
# , когда акция стоила дешевле всего и номер дня, когда стоила дороже всего)
# prices = np.array([150, 142, 165, 139, 155])
# min_index = np.argmin(prices)
# max_index = np.argmax(prices)
# print(f"минимальная цена (индекс): {min_index}")
# print(f"максимальная цена (индекс): {max_index}")

# import pandas as pd

# s1 = pd.Series([1,2,3,4,5])
# s2 = pd.Series([6,7,8,9,10])
#
# # s3 = s1 + s2
# # print(s3)
#
# # s3 = s2 - s1
# # s3 = s2 * s1
# s3 = s2 / s1
# print(s3)

# s1 = pd.Series(['a','b','c', 'w', 'r'])
# s2 = pd.Series(['d','e','f'])
#
# s3 = s1 + s2
# print(s3)

# s1 = pd.Series([1,2,3,4,5])
# s2 = s1 + 5
#
# print(s2)

# s = pd.Series([10,20,30,40,50])
#
# filtered_data = s[s >= 30] # 30, 40, 50 с сохранением своих меток
# print(filtered_data)

# s = pd.Series(['Сергей', 'Роман', 'Вадим','Виталий','Сергей', 'Вадим'])
# filtered_data = s[s == 'Сергей']
# print(filtered_data)

# s = pd.Series([1,2,3,5,8,13,21,30,55,89])
#
# # filtered_data = s[(s > 8 ) & (s < 30)] #
# filtered_data = s[(s > 8 ) | (s < 30)] # False | True если или хотя бы с одной строны долно быть тру
# print(filtered_data)

# s = pd.Series(['Сергей', 'Роман', 'Вадим','Виталий','Александр', 'Артем'])
# filtered_data = s[s.isin(['Роман', 'Игорь', 'Артем'])] # позволяет проверить соответствует ли элемент указанным значениям
# print(filtered_data)

# s = pd.Series([1,2,3,5,8,13,21,30,55,89])
# data_filtered = s[s.between(8,30)] # фильтруются от 8 до 30 включительно
# print(data_filtered)

# s = pd.Series(['1.0', '2', 'ошибка', '4.5'])
# # res = pd.to_numeric(s, errors='coerce') # если есть строковое значение
#
# # s = pd.Series(['1.0', '2', '4.5'])
# # res = pd.to_numeric(s)
# #
# # print(res)
#
# # res = s.astype(int)  # если знает тип данных эд
# res = s.astype(int, errors='ignore') # преобразовываем к числу
# print(res)

# data = {
#     'Name': ['Сергей', 'Анна', 'Роман', 'Александр'],
#     "Age": [28, 35, 23, 42],
#     'City':['Сочи','Москва','Воронеж','Армавир']
# }
# df = pd.DataFrame(data)
# print(df)
# print('*' * 30)
# cities = (df['City']) # 1 вариант обратились по ключу и получили все знаяения столбца
# print(cities)
#
# print('*' * 30)
# cities = df.City # 2 вариант обратились по ключу и получили все знаяения столбца
# print(cities)
#
# print('*' * 30)
# columns = ['City', 'Name'] # сохранили в переменную колонки
# print(df[columns]) # полчили доступ к значениям колонок
#
# # print(df[['City', 'Name']]) # 2 вариант получить доступ к значениям 2м колонок
# print('*' * 30)
# int_columns = df.select_dtypes(include='int64') #обращаемся к числовым значениям
# # и он вывел все солбцы с числовыми значениями
# print(int_columns)

#Общий вывод:
# df = pd.DataFrame(data) #
# print(df)
# print('*' * 30)
# print(df.loc[1]) # вывели строку обратившись к индексу/метке 1
# print(df.loc[0:2]) # вывели строку обратившись к индексу/метке в диапазоне
# =====================

# df = pd.DataFrame(data, index=['str_1', 'str_2', 'str_3', 'str_4']) #замена индексов 0,1,2,3 на значения str_1 и т.д.
# print(df)
# print('*' * 30)
# # print(df.loc['str_2']) # вывели строку обратившись к 'str_2'
# print(df.loc[['str_1','str_3']]) # вывели строку обратившись к 'str_2'
# print(df.loc['str_1':'str_3']) # вывели c 'str_1':'str_3' включительно
# print(df.iloc[0])
# print('*' * 30)
# # print(df.iloc[1:3]) #1 вариант
# print(df[1:3]) #2 вариант

# print(df['City']['str_3'])
# print('*' * 30)
# print(df['City'][1:3]) #Москва Воронеж по индексам
# print('*' * 30)
# print(df['City']['str_2':'str_4']) #Москва Воронеж по индексам включительно 2 и 4
# print(df['City'][['str_1','str_3', 'str_4']]) #

# column = ['City', 'Name']
# print(df[column][1:3]) # указали в диапазоне колонок какой срез нужен н
#
# print(df[['City', 'Name']][1:3]) #
#
# print(df.shape) # (4, 3) 4 строки и 3 столбца

# print(df.dtypes) # по каждому столбцу показывает тип данных и в конце общий тип
#
# rows = [
#     ['Ноутбук', 50000, 5],
#     ['Смартфон', 30000, 10],
#     ['Наушники', 5000, 25]
# ]
# df_products = pd.DataFrame(rows, columns=['Товар', 'Цена', 'Количество' ]) # дали названия колонок если не словарь
# print(df_products)
#
# print('*' * 30)
#
# api_data =[
#     {'ФИО': 'Иванов И.И.', 'Департамент': 'IT'},
#     {'ФИО': 'Петров П.П.', 'Департамент': 'HR'},
#     {'ФИО': 'Сидоров С.С.'}
# ]
#
# df = pd.DataFrame(api_data)
# print(df)

# import  numpy as np
# import pandas as pd
#

# data = np.array([
#     ['Том',41, 'Yandex'],
#     ['Bob', 56, 'VK'],
#     ['Sam',31, 'Sber']
# ])
# #преобразорвывем нампай в пандас:
# columns  = ['Name', 'Age', 'Company' ]
# df= pd.DataFrame(data, columns=columns)
# print(df)


# data = pd.read_excel('data.xlsx') # когда считываем данные из экселя он автоматически как датафрейм
# print(data)
# print('*' * 50)
# # print(data.head(3)) # вывели первые 3 записи
# print(data.tail(3)) # вывели последние 3 записи
# print(data.Age.describe()) # все статистические данные по столбцу Age
# print('*' * 50)
# print(data.describe())


# df = pd.read_json('people.json')
# print(df)

# df = pd.read_csv('internet.csv')
# print(df)
# print('*'* 50)
# # print(df.sort_values('mobile', ascending=False)) # сортировка по убываю
# # print(df.dropna())
#
# new_country = {'country': 'Галактика', 'broadband': 1234, 'mobile': 295.45}
# df1 = pd.DataFrame([new_country])
# print(df1)
# print('*'* 50)
#
# new_list1 = pd.concat([df1, df], ignore_index=True) # сделали новые индексы после объединения
# print(new_list1)
# # new_list1.to_csv('country.csv')
# new_list1.to_csv('new_country.csv', index=False)


# import pandas as pd
#3326 Задача 1: Создание Series и фильтрация
# Условие: у вас есть данные о продажах товаров в интернет-магазине
# за неделю (в тысячах рублей): [12, 15, 8, 20, 25, 30, 10].
# Дни недели соответствуют индексу: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'].
# Создайте Series и найдите дни, когда продажи были больше 15 тысяч рублей.
# s_data = [12, 15, 8, 20, 25, 30, 10]
# s_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# sales = pd.Series(s_data,index=s_days)
# print(sales)
# print('*'* 10)
# filtered_data = sales[sales > 15]
# print(filtered_data)

#-------------------------------------------

#Задача 2: Поиск топ-N значений
# Условие: Дан список оценок студентов по тесту: [85, 90, 78, 92, 88, 76, 95, 92].
# Индексы — имена студентов: ['Аня', 'Боря', 'Влад', 'Глаша', 'Дима', 'Ева', 'Жора', 'Зина'].
# Найдите 3 самые высокие оценки.
# s_score = [85, 90, 78, 92, 88, 76, 95, 92]
# s_name = ['Аня', 'Боря', 'Влад', 'Глаша', 'Дима', 'Ева', 'Жора', 'Зина']
# res_student = pd.Series(s_score,s_name)
# print(res_student)
# print('*'* 20)
# sorted_scores = res_student.sort_values(ascending=False) # сортируем по убыванию
# # print(sorted_scores)
# filtered_top = sorted_scores.head(4) # выводим топ 3 (два студента с одним результатом)
# print(filtered_top)

#-------------------------------------------

#Задача 3: Проверка условий (True / False)
#Условие: Дан Series с возрастом пользователей: [16, 25, 38, 17, 42, 15].
# Создайте новый Series, который будет содержать True,
# если пользователь совершеннолетний (18 лет и старше), и False, если нет.
#
# s = [16, 25, 38, 17, 42, 15]
# age = pd.Series(s)
# filtered_age = age >= 18
# print(filtered_age)

#
# df = pd.read_csv('internet.csv')
# print(df)
# print('*'* 50)
# print(df.sort_values('mobile', ascending=False)) # сортировка по убываю
# print(df.dropna())

# new_country = {'country': 'Галактика', 'broadband': 1234, 'mobile': 295.45}
# df1 = pd.DataFrame([new_country])
# print(df1)
# print('*'* 50)
#
# new_list1 = pd.concat([df1, df], ignore_index=True) # сделали новые индексы после объединения
# print(new_list1)
# new_list1.to_csv('country.csv')
# new_list1.to_csv('new_country.csv', index=False)
# new_list1.to_csv('new_data.txt', index=False)
# new_list1.to_string('new_data1.txt', index=False)
# print('*'* 50)
# new_list1.drop(0, inplace=True) # удалили по индексу
# print(new_list1)


# df = pd.read_csv('internet.csv') # csv становится DataFrame через пандас - обращение pd...
# print(df)
# print('*'* 50)
# print(df[df['mobile'] > 100]) # сравниваем со значением 100
# filtred_data = df[df['country'].str.startswith('S')] # фильтр стран с "S"
# print(filtred_data)
#
# print(df['broadband'].agg(['mean'])) # среднее ариф
# print('*'* 50)
# print(df['broadband'].agg(['min', 'max', 'median']))
#Способы вывода(представленя данных) df:

# в цикле (перебор по столбцам):
# for row_label, row in df.items(): # items() берет и ключи и значения одновременно
#     print(row_label, row, sep="\n", end="\n\n")
# print('*'* 50)

# в цикле  (перебор по строкам):
# for row_label, row in df.iterrows():
#     print(row_label, row, sep="\n", end="\n\n")

# в цикле  (выводит в виде кортежа) в строку:
# for item in df.itertuples():
#     print(item, sep="\n", end="\n\n")

#
# data = {
#     'User_ID': [101, 102, 101, 103, 101],
#     'City': ['Москва', 'Питер', 'Москва', 'Казань', 'Сочи'],
#     'Spend': [500, 700, 500,300 ,1200]
# }
# df = pd.DataFrame(data)
# print(df)
#
# print('*'* 50)
# duplicates = df.duplicated() # поиск дубликтов
# print(duplicates)
#
# print('*'* 50)
# df_cleaned = df.drop_duplicates().reset_index(drop=True) # находит и удаляет дубликаты,
# # а reset_index(drop=True) сбросил индексацию
# print(df_cleaned)
# df_cleaned = df.drop_duplicates(subset='User_ID', keep='last') # удалили дубликаты по столбцу User_ID
# print(df_cleaned)
# print(df)
# print('*'* 50)
# df.drop_duplicates(inplace=True) #изменение в исходном DF
# print(df)

# year = [1147, 1703, 1723,1893, 1589]
# df['Year'] = year
# print(df)

# new_columns = pd.DataFrame({
#     "Year": [1147, 1703, 1723,1893, 1589],
#     "Time zone": ['GMT+3','GMT+3', 'GMT+3', 'GMT+3', 'GMT+3' ]
# })
# print('*'* 50)
# df = pd.concat([df, new_columns], axis=1) #
# print(df)
# print('*'* 50)
#
# df.drop('Year',axis=1, inplace=True)
# print(df)
# print('*'* 50)

# new_row = pd.Series([104, 'Воронеж', 1042], index=df.columns)
# print(new_row)
# print('*'* 50)
# df.loc[len(df)] = new_row # в последнюю строк  добавили
# print(df)
# print('*'* 50)
#
# new_row  = pd.DataFrame([[104, 'Воронеж', 1042], [105, 'Саратов', 542]], columns=df.columns)
# df = pd.concat([df, new_row], ignore_index=True) # добавиил 2 строки
# print(df)
# print('*'* 50)
# rows = [1, 3]
# df.drop(rows, inplace=True) # удалили строку с индексоми в переменной rows = [1, 3]
# # df.drop(2, inplace=True) # удалили строку с индексом 2
# print(df)

#методы пандас:
# data = {"Age": [34,37,13,64,37,47,24,38,26,41,19,51,44]}
# df = pd.DataFrame(data)
# print(df)
# print('*'* 50)
# print("Среднее значение:", df["Age"].mean())
# print('*'* 50)
# print("Медиана:", df["Age"].median())
# print('*'* 50)
# print("Мода", df["Age"].mode()[0]) #
# print('*'* 50)
# print("Разброс значений", df["Age"].var(), 'и стандартное отклонение:', df["Age"].std() ) #
# print('*'* 50)
# print("Квантили возраста:") #
# print(df["Age"].quantile([0.25, 0.5, 0.75]))
# print('*'* 50)
# print('90-й процентиль возраста:',df["Age"].quantile([0.90]))

# import numpy as np
# import pandas as pd


#
# data = {
#     "A":[1,2,np.nan, 4, None],
#     "B":[None, 6,7,8,np.nan]
# }
#
# df = pd.DataFrame(data)
# print("DataFrame до заполнения пропущенных значений: ")
# print(df)
# print('*'* 50)
# # # # Метод isna для поиска пропущунных значений:
# # missing_data = df.isna() # True - если элемент отсутствует
# # print(missing_data)
# # print('*'* 50)
# # non_missing_data = df.notna()# False - если элемент отсутствует
# # print(non_missing_data)
# print("DataFrame после заполнения пропущенных значений: ")
# # print('*'* 50)
# # filled_df = df.fillna(0) # заполнил знаяения NaN значением 0.0
# # print(filled_df)
# filled_df = df.copy() # создали копию чтобы не влиять на оригинал
# filled_df["A"] = df["A"].fillna(df['A'].mean()) # заполнил где NaN в столбце A среднеариф
# print(filled_df)
#
# filled_df = df.copy() # создали копию чтобы не влиять на оригинал
# filled_df["B"] = df["B"].fillna(df['B'].median()) # заполнил где NaN в столбце B медианой
# print(filled_df)

#================================================
# data = {
#     "City": ["Москва", "Санкт-Петербург", "Новосибирск","Екатеринбург","Казань","Краноярск", "Волгоград" ],
#     "Population": [13274, None, 1637, None, 1330, 1212, None],
#     "Time zone": ['GMT+3','GMT+3', 'GMT+7', 'GMT+5', 'GMT+3',None, 'GMT+3']
# }
#
# df = pd.DataFrame(data)
# print(df)
# print('*'* 50)
# # missing_data = df["Population"].isna() # возращает булево значение - True, если NaN
# # print(missing_data)
# # print('*'* 50)
# # missing_data = df[df["Population"].isna()] # возращает только Population с NaN
# # print(missing_data)
# # print('*'* 50)
# # missing_mask = df.isna() # возращает все строки с NaN по всем столбцам
# # missing_data = df[missing_mask.any(axis=1)]
# # print(missing_data)
# print('*'* 50)
# not_missing_mask = df.notna() # получаем знаяения без NaN (пропусков)
# non_missing_df = df[not_missing_mask.all(axis=1)]
# print(non_missing_df) # если заполнено -  True, если значение отсутвует - False


# print("DataFrame до заполнения пропущенных значений: ")
# print(df)
# print('*'* 50)
# # Обработка пустых значений:
# tz_mod = df['Time zone'].mode()[0]
# print('Мода для столбца Time zone',tz_mod)
# print('*'* 50)
# print("DataFrame после заполнения пропущенных значений: ")
#
# df['Time zone'] = df['Time zone'].fillna(tz_mod) # нашли пустые значения NaN и передаем значения моды из tz_mod
# print(df)
# print('*'* 50)

#
# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга', 'Марина', 'Роман', 'Екатерина', 'Виктор', 'Ирина'],
#     'Возраст': [25, 34, 41, 28, 19, 20, 36, 41, 38],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи', 'Санкт-Петербург', 'Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
#
# df = pd.DataFrame(data)
# print(df)
# print('*'* 50)
# print(df.groupby('Город')['Возраст'].median()) # делает группировку по определенному параметру
# print(df.groupby('Город')['Возраст'].sum()) # делает группировку по определенному параметру

#---------------------------22.10
# data = {
#     "product_id":[105, 111, 102,108,123,105],
#     'category':[
#         ' Электроника ',
#         "Одежда",
#         " Электроника",
#         "Обувь",
#         "Одежда ",
#         ' Электроника '
#     ],
#     'price':["15 000,50", "2 500,00", "Не указана", "1 200", None, "15 000,50"],
#     'quantity': [2, np.nan, 1, 5, 10, 2]
# }
# df = pd.DataFrame(data)
# print(df)
# print('*' * 60)
# df['category'] = df['category'].str.strip() #убрали пробелы и слева и справа
# # print(df)
# df['price'] = df['price'].str.replace(' ', '') # убрали лишние пробелы в цифрах
# # print(df)
# # print('*' * 50)
# df['price'] = df['price'].str.replace(',', '.')# убрали запятые и заменили на . в числах
# # print(df)
# # print('*' * 50)
# df['price']=pd.to_numeric(df['price'], errors = 'coerce') #преоюразовали к числовым значениям
# # print(df)
# # print('*' * 50)
# df['price'] = df['price'].fillna(df['price'].median()) # ЗАПОЛНИЛИ ПРОПУСКИ  МЕДИАННЫМ ЗНАЧЕНИЕМ
# # print(df)
# # print('*' * 50)
# df['quantity'] = df['quantity'].fillna(1) #  NaN в столбце  quantity заменили на 1
# # print(df)
# # print('*' * 60)
# df['total_revenue'] = df['quantity'] * df['price'] # добавили новый столбец
# # print(df)
# # print('*' * 60)
# df = df.drop_duplicates().reset_index(drop=True) # удалили дубликаты и пересчитали индексы
# print(df)
# print('*' * 60)

#====================
# import pandas as pd
#
#
# df = pd.read_csv('platforms.csv') #рочитаи файл platforms.csv
# print(df, end='\n\n')
# print('*' * 60)
#
# df['Views'] = df['Views'].fillna(df['Views'].mean()) # заменили  NaN на среднеариф.
# print(df, end='\n\n')
# print('*' * 60)
# df['Revenue'] = df['Revenue'].fillna(0) # заменили  NaN на 0
# df.drop_duplicates(inplace=True) #удалили элементы дубликаты
# print(df, end='\n\n')
# print('*' * 60)
# df['Views'] = df['Views'].astype(int) #преобразовали в целочисленное значение
# df['Date'] = pd.to_datetime(df['Date']) #преобразовали в дату
# print(df, end='\n\n')
# print('*' * 60)
#
# print(df.describe(), end='\n\n') # метод работает только с числовыми данными и датами
# filtered = df[df['Platform'] == 'YouTube'] #отфильтровали данные и вывели только данные по YouTube
# print(filtered, end='\n\n')
#
# mean_views = filtered['Views'].mean()
# mean_revenue = filtered['Revenue'].mean()
# print(mean_views, end='\n\n')
# print(mean_revenue, end='\n\n')
#
# filtered.to_csv('new_data.csv', index=False)

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([4, 5, 6, 7, 8]) # преобразует обычный список Python в массив NumPy
# y = np.array([1, 2, -6, 0, 4])
# # plt.plot([1,2,-6,0,4]) # по оси Y (по оси ординат)
# plt.plot(x,y)
# plt.show()

# x = np.array([1, 1, 5,  5, 1]) # преобразует обычный список Python в массив NumPy
# y = np.array([1, 5, 5, 1, 1])
# plt.plot(x,y)
# plt.show()

#из массива NumPy:
# y = np.array([0,1,2,3,4,])
# x = np.array([a * a for a in y]) # [ 0  1  4  9 16]
# print(x)
# plt.plot(x,y)
# plt.grid()
# plt.show()

# из обычного массива:
# plt.plot([1,2,3], [4,5,2], [1,2,4], [5,3,6])
# plt.plot([1,2,3], [4,5,2]) # x, y
# plt.plot([1,2,4],[5,3,6]) # x, y
# plt.grid()
# plt.show()

# plt.plot([1,2,4],[4,2,5], '--') #график в виде ----
# # plt.plot([1,2,4],[4,2,5], ':')
# # plt.plot([1,2,4],[4,2,5], '-.')
# plt.show()

# plt.plot([1,2,4], [4,2,5], '-.', [1,2,3], [3,6,5], ':')

# plt.plot([1,2,4], [4,2,5], '-.', color='red') # установили цвет графика
# plt.plot([1,2,4], [4,2,5], '-.', color='#FF0000')
# plt.plot([1,2,4], [4,2,5], '-.', color='#F00')
# plt.plot([1,2,4], [4,2,5], '-.o', c='#F00') # добавили маркеры чарез '-.o'
# plt.plot([1,2,4], [4,2,5], '-.', c='#F00', marker='s', markerfacecolor='#0F0', linewidth=4) # добавили маркеры чарез '-.o'
# plt.grid() # добавление сетки
# plt.show()



# x = [1,2,4]
# y = [4,2,5]
# x1 = [1,2,4]
# y1 = [3,4,4]
# plt.plot(x,y, color='green', label='линия 1')
# plt.plot(x1,y1, color='orange', label='линия 2')
# plt.fill_between(x1, y1, y, color='yellow', alpha=0.3, label='область между ними')
# plt.title('Заливка между линиями') #заголовок графика
# plt.xlabel('Ось х')
# plt.ylabel('Ось y')
# plt.legend()# дбави ли легенду-подпись
# plt.minorticks_on() # минорная сетка
# plt.grid(which='major', linewidth='1', color='#444')
# plt.grid(which='minor', color='#aaa',ls=':')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots() # фигура и график на холсте(объект мольберта - fig)
# #
# # ax.plot([1,2,3], [4,5,2])
# # ax.set_title('Мой график')
# # plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# days = np.array(list(range(1,8))) # [1 2 3 4 5 6 7] - массив с кол-ворм дней недель
# # print(days)
# temperature = [20,22,21,26,28,23,24]
#
# fig, ax = plt.subplots()
# ax.set_xlabel('День')
# ax.set_ylabel('Температура', fontsize = 14) # Увеличили шрифт подписи
# ax.set_title('Динамика температуры за неделю', fontsize = 16, fontweight='bold', color = 'blue', loc='right') # добавлен заголовок
#
# ax.set_yticks([20,22,21,26,28,23,24])
# ax.set_yticklabels(['20°','22°','21°','26°','28°','23°','24°'])
#
# ax.set_xticks(days)
# ax.set_xticklabels(['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'])
#
# ax.tick_params(axis='x', length=7, labelsize=20) # rotation=90 - развернули подписть ПН, ВТ.. на 90 градусов
# # ax.grid(axis='y') # добавлена сетка по оси y
# # ax.grid(axis='both') # добавлена сетка-клетка
# ax.grid(True, which='major',axis='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7) # добавлена сетка-клетка
#
# ax.text(5,28, 'Макс значение', fontsize=14, color='red', va='top', ha='right')
#
# ax.plot(days,temperature, label='Температура')
# ax.legend(loc='lower right', fontsize=12, framealpha=0.8) # сверху слева легенда
#
# plt.show()


# ----------------24.10 Диаграмма рассеивания
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


# Диаграмма рассеивания:
# x = np.array([np.random.randint(0,10) for i in range(100)])
# y = np.array([np.random.randint(0,10) for i in range(100)])
#
# plt.scatter(x, y, color='red', alpha=0.5)
# plt.xlabel('переменная x')
# plt.ylabel('переменная y')
# plt.title('Диаграмма рассеивания')
#

# plt.show()

#------
# districts = np.array([i for i in range(10) for j in range(20)])
# # print(districts)
#
# base_prices = [65,80,75,35,90,55,40,110,95,70]
# prices = [
# base_prices[d] + np.random.randint (-10, 10) for d in districts
# ]
# # print(prices)
# df = pd.DataFrame({'District':districts, 'Price':prices })
#
# mean_price = df.groupby('District')['Price'].mean()
# cheapest_districts = mean_price.nsmallest(2).index.tolist()
# print(f'Самые дешевые районы: {cheapest_districts}')
#
#
# cheapest_df = df[df['District'].isin(cheapest_districts)]
# other_df = df[~df['District'].isin(cheapest_districts)]
#
# plt.figure(figsize = (10,6))
#
# plt.scatter(
#     other_df['District'],
#     other_df['Price'],
#     color='lightgrey',
#     alpha = 0.7,
#     edgecolor = 'black',#рамка вокруг точки
#     linewidth = 0.5, # прозрачность рамки 50%
#     label = 'Остальные районы'
# )
#
# plt.scatter(
#     cheapest_df['District'],
#     cheapest_df['Price'],
#     color='red',
#     alpha = 0.9,
#     edgecolor = 'black',#рамка вокруг точки
#     s = 70, #увеличили точки
#     label = 'Два самых дешевых района'
#
# )
#
# plt.title('Распределение цен на квартиры по районам города', fontsize=14, fontweight='bold')
#
# plt.xlabel('Номер района', fontsize=12)
# plt.ylabel('Цена квартиры (млн. руб.)', fontsize=12)
# plt.grid(axis='y', linestyle='--', alpha=0.5) #сетка
#
# plt.legend()
#
# plt.show()

#---------Hist (Гистограмма)

# age_data = [np.random.randint (18, 55) for i in range(25)]
# print(age_data)
#
# plt.hist(age_data, bins=10, edgecolor='black', color='orange') # разбивка на интервалы с шагом 5
#
# plt.title('Возраст зрителей в кинотеатре')
# plt.xlabel('Возраст (лет)')# подписи осей
# plt.ylabel('Количество человек')# подписи осей
#
# plt.show()

#---------Hist (Гистограмма) на примере доставки пиццы
# import random
# delivery_times = [random.gauss(35.0, 7.0) for i in range(1000)] #генерим список на 1000
# # заказов c доставокой +-7 от 35мин
#
# plt.figure(figsize=(9,5))
#
# plt.hist(delivery_times,
#          bins=20,
#          color='#3498db',
#          edgecolor='white',
#          alpha=0.8
# )
#
# plt.axvline(x=40,color='red', linestyle='--', linewidth=2, label='Стандарт компании (40 минут)')
#
# plt.title('Анализ времени доставки пиццы (1000 заказов)', fontsize=14, fontweight='bold')
#
# plt.xlabel('Время доставки в минутах', fontsize=12)
# plt.ylabel('Количество заказов', fontsize=12)
# plt.grid(axis='y', linestyle=':', alpha=0.5)
# plt.legend(loc='upper left')
#
# plt.legend()
# plt.show()


#-----Bar (Столбчатые диаграммы):
# categories = ['Пицца', 'Бургеры', 'Суши', 'Салаты', 'Напитки']
# sales = [120, 85, 95, 40, 150]
#
# plt.figure(figsize=(8,5))
# plt.bar(categories, sales, color='#1f77ff', edgecolor='#0000BB',width=0.6)
#
# plt.title('Продажа блюд в кафе за день', fontsize = 14, fontweight = 'bold')
# plt.xlabel('Категории меню', fontsize=12)
# plt.ylabel('Количество проданных порций', fontsize=12)
#
# plt.grid(axis='y', linestyle='--', alpha=0.5)
#
# plt.show()


#-----Bar (Столбчатые диаграммы) на примере языков програмирования:

# languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'Go', 'PHP']
# project_count = [45,38,29,22,15,12,8]
#
#
# colors = ['purple' if i == 0 else '#b0bec5' for i in range(len(languages))]
#
# plt.figure(figsize=(9,6))
#
# bars= plt.bar(languages,project_count, color= colors)
#
# plt.title('Использование языков програмирования в компании', fontsize = 14, fontweight = 'bold')
# plt.xlabel('Языки програмирования', fontsize=12, labelpad = 10)
# plt.ylabel('Количество активных проектов', fontsize=12, labelpad = 25)
#
# plt.ylim(0, max(project_count) + 5)
#
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.gca().spines['top'].set_visible(False)
# plt.gca().spines['right'].set_visible(False)
# plt.tight_layout()
#
# plt.show()

#------------------
# days = [1,2,3,4,5]
#
# works = [5,4,6,5,4]
# rest= [3,4,2,3,4]
# sleep = [5,7,10,9,8]
#
# plt.stackplot(days,works,rest,sleep, labels=['Работа', 'Отдых', 'Сон'],
#               colors=['#4466ee','#00bbff','#ff9988'])
# plt.title('Распределение времени за 5 дней')
# plt.xlabel('Дни')
# plt.ylabel('Часы')
# plt.grid(alpha=0.3)
#
# plt.legend()
# plt.show()

#------------------
#
# mouths = pd.date_range(start='2026-01-01', end='2026-12-31', freq='MS')
# print(mouths)
#
# laptops = [500, 5800, 3000, 3500, 3500, 3800, 6100, 6500, 6600, 6600, 6800,5000]
# smartphones = [2500, 166,2700,1800,2900,5000,5100,5500,5300, 5600,5500,5600]
# tablets = [1000,1500,1600,1600,1800,5000,5500,5600,5600,5800,3000,3500]
#
# df = pd.DataFrame({'Month': mouths.strftime('%b %Y'), 'Laptops': laptops, 'Smartphones': smartphones, 'Tablets': tablets})
#
# plt.figure(figsize=(12,6))
# plt.stackplot(df['Month'], df['Laptops'],df['Smartphones'],df['Tablets'], labels=['Ноутбуки', 'Смартфоны', 'Планшеты'])
#
# plt.title('Общие ежемесячные продажи за год')
# plt.xlabel('Месяц')
# plt.ylabel('Общие продажи')
# plt.grid()
#
# plt.legend()
# plt.show()

#Круговая диаграмма
#
# labels = ['Еда', 'Транспорт', 'Жилье', 'Развлечения']
# sizes = [30,20,40,10]
#
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow'])
#
# plt.title('Круговая диаграмма')
#
# plt.show()


# sizes = [35,25,25,15]
# labels=['Python', 'JavaScript', 'C++', 'Java']
# colors = ['#ff9999', '#66bbff', '#99ff99','#ffcc99']
#
# explode = [0.1,0,0,0] # отодвинули самый большой сегмент
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140)
#
# plt.title('Популярность языков програмирования')
# plt.show()


#------------25.10!Bxplot (Диаграмма размаха) (Ящик с усами)
#
# age = [22,24,26,28,29,30,31,32,35,38,41,45,65]
#
# plt.boxplot(
#     age,
#     patch_artist=True, #разрешит закрасить внутренность ящика
#     widths=0.15, # меняет ширину ящика
#     flierprops=dict(marker='o', markersize=10,
#                     markeredgecolor='#ff4dd4', markerfacecolor='#ff9999', alpha=0.8),
#     medianprops=dict(color='#ff4d4d', linewidth=3), #  линия внутри ящика
#     boxprops=dict(facecolor='#99ccff', color='#4d4d4d', linewidth=1),#цвет ящика и толщина лний
#     whiskerprops=dict(color='#0000FF', linewidth=1), # цвет усов
#     capprops=dict(color='#0000FF', linewidth=1),
# )
#
# #Оформление текстом:
# plt.text(1.1,30, 'Медиана', va='center', ha='left')
# plt.text(1.1, 22, 'Мин (22)', va='center', ha='left')
# plt.text(1.1, 65, 'Выброс (65)', va='center', ha='left', color='#cc6666', fontsize=11)
# plt.grid(axis='y', linestyle='--', color='#CCCCCC') # вспомогательная сетка
#
# #подписи осей:
# plt.title("распределение возраста сотрудников")
# plt.ylabel('Возраст(лет)')
# plt.xlabel('Сотрудники')
#
# #удаление лишних надписей на оси:
# plt.xticks([1], [' '])
#
# plt.show()

#
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1,2,3])
# y = np.array([1,2,3])
#
# x, y = np.meshgrid(x, y)
#
# z = x + y
#
# fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
#
# ax.plot_surface(x,y,z)
#
# plt.show()

# price = np.array([10, 20, 30, 40, 50])
# customers=np.array([100, 200, 300, 400, 500])
#
# x, y = np.meshgrid(price, customers)
#
# z = x * y
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d') # 1 - строк, 1 - сколько колонок. 1 - номер графика который создем
#
# ax.plot_surface(x, y, z,cmap='viridis') # jet, viridis
# ax.set_xlabel('Модель прибыли')
# ax.set_xlabel('Цена товара($)')
# ax.set_ylabel('Количество клиентов')
# ax.set_zlabel('Прибыль ($)')
#
# plt.show()

#тепловая карта:
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# data = np.array(np.array([[np.random.randint(-2, 3) for i in range(5)]for i in range(15)]))
#
# df = pd.DataFrame(data, columns=['Возраст', 'Доход', 'Кредит', 'Покупки', 'Дети'])
# print(df)
#
# print('*' * 50)
#
# df.iloc[2,0] = np.nan
# df.iloc[5:8,1] = np.nan
# df.iloc[12,2]= np.nan
# df.iloc[1,3]= np.nan
# df.iloc[7:10,4]= np.nan
#
#
# print(df)
#
# misssing_matrix = df.notna().astype(int)
# print('*' * 50)
# print(misssing_matrix)
#
# plt.figure(figsize=(8,6))
# plt.imshow(misssing_matrix, aspect='auto')
#
# cbar = plt.colorbar(ticks=[0,1])
# cbar.ax.set_yticklabels([' Пропуск (nan)', 'Есть данные'])
#
# plt.xticks(range(len(df.columns)), df.columns, rotation=45, ha='right') # вместо индексов названия колонок
# plt.yticks(range(len(df)))
#
# plt.title('Карта пропущенных значений в датасете')
# plt.xlabel('Признаки (колонки)')
# plt.ylabel('Индексы строки (записи)')
#
# plt.show()


#-----------------
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# days = ['пн', 'вт', 'ср', 'чт','пт','сб','вс']
# hours = [f'{h:02d}:00' for h in range(9, 21)] # включая с 9 до 20
#
# # создать матрицу случайных активнойстей:
# data = np.random.randint(5,40, size=(len(hours), len(days)))
# data[3:5,0:5] += 25
# data[7:11,5:7] += 45
#
#
# plt.figure(figsize = (9,7))
#
# im = plt.imshow(data, aspect='auto', cmap='Oranges')
# for i in range(len(hours)):
#     for j in range(len(days)):
#         val = data[i, j]
#         color = 'white' if val > 45 else 'black'
#         plt.text(j, i, str(val), ha='center', va='center', color=color, fontsize=10)
# plt.xticks(range(len(days)), days) # заменили шкалу на дни недели
# plt.yticks(range(len(hours)), hours) # заменили шкалу на часы
#
# cbar = plt.colorbar(im)
# cbar.set_label('Количество дней / покупок', labelpad=10)
#
# plt.gca().set_xticks(np.arange(-0.5, len(days), 1))
# plt.gca().set_yticks(np.arange(-0.5, len(hours), 1))
#
# plt.grid(which='minor', color='black', linestyle='-', linewidth=1.5)
# plt.tick_params(which='minor', bottom=False, left=False)
#
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# объединение графиков

# x = np.array(list(range(1,13)))
# print(x)
#
# y1 = np.random.randint(50, 200, size=12)
# y2 = np.random.randint(50, 200, size=12)
#
# fig, ax = plt.subplots()
#
# ax.plot(x, y1, label='Общие продажи', color='blue')
# ax.scatter(x,y2, label='Характеристика пиковых продаж', color='red')
# ax.bar(x, y1, alpha=0.3, label='Распределение продаж', color='violet')
#
# ax.legend()
# plt.show()

#-----------------------

# import 0pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,8))
#
# x = np.array(list(range(1,6)))
# y1 = [1,4,9,16,25]
# y2= [2,3,5,7,11]
#
# ax[0][0].plot(x,y1, color='blue')
# ax[0][0].set_title('Линейный график')
#
# ax[0, 1].scatter(x,y2, color='red')
# ax[0, 1].set_title('Диаграмма рассеивания')
#
# ax[1, 0].bar(x,y1, color='green')
# ax[1, 0].set_title('Столбчатая диаграмма')
#
# ax[1, 1].hist(np.random.random(100), bins=15, color='purple')
# ax[1, 1].set_title('Гистограмма')

# plt.show()
# plt.savefig('chart.png')
# plt.savefig('chart_3.png', dpi=300, bbox_inches='tight', facecolor='none', edgecolor='none')
# plt.savefig('chart_5.pdf', bbox_inches='tight')
# plt.savefig('chart_6.svg', bbox_inches='tight')
# plt.savefig('chart_7.jpeg, dpi=300, bbox_inches='tight')

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme(style="darkgrid", context="talk")
# tips = sns.load_dataset("tips")
# print(tips.head())
#
# # datsets = sns.get_dataset_names()
# # print(datsets)
#
# plt.figure(figsize=(10,5))
# sns.histplot(data=tips, x='total_bill', bins=30)
# plt.title('Распределение счетов')
# plt.xlabel('Общая сумма счета($)', fontsize=11)
# plt.ylabel('Чаевые($)', fontsize=11)
#
# plt.show()


##28.10
#
# import matplotlib.pyplot as plt
# import seaborn as sns

# tips = sns.load_dataset("tips")
# print(tips.head())
#
# plt.figure(figsize=(10, 6))
# # sns.boxplot(tips, x="day", y="total_bill")
# sns.boxenplot(tips, x="day", y="total_bill",
#               palette = 'viridis',
#               linewidth=2,
#               width=0.8,
#               k_depth='proportion',
#               order=["Fri", "Sat", "Sun",'Thur']
#               )
#
# plt.title('Распределение счетов по дням')
# plt.xlabel('День недели', fontsize=11)
# plt.ylabel('Общая сумма счета ($)', fontsize=11)
# plt.grid(alpha=0.3)
#
# plt.show()
#
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue='smoker')
# plt.title('Зависимость чаевых от счета')


# corr_matrix = tips.corr(numeric_only=True)
# sns.heatmap(corr_matrix, annot=True,cmap="coolwarm", fmt='.2f') #подписали значения через annot=True
# plt.title("Корреляционная матрица")
#
# plt.show()
#
# import matplotlib.pyplot as plt
# import seaborn as sns

# iris = sns.load_dataset("iris")
# print(iris.head())
#
# sns.pairplot(iris, hue="species")
# plt.show()

# titanic = sns.load_dataset("titanic")
# print(titanic.head())
#
# plt.figure(figsize=(10,6))
#
# sns.countplot(data=titanic, x='class', hue='survived')
# plt.title('Выживаемость по классам')
#
# plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# tips = sns.load_dataset("tips")
# print(tips.head())
# # plt.figure(figsize=(10,6))
# # sns.violinplot(data=tips, x="day", y="total_bill", palette='husl', hue='day')
# # plt.title('Распределение счетов(violin plot)')
# # plt.show()
#
# # sns.barplot(x='day', y ='total_bill', data=tips, estimator=np.mean)
# # plt.title('Средний счет по дням')
#
# sns.kdeplot(data=tips, x='total_bill', fill=True, hue='smoker',alpha=0.8, palette='Set2')
# plt.figure(figsize=(10,6))
# # plt.title('Плотность распределения счетов')
# plt.title('Распределение счетов: курящие vs некурящие')
# plt.xlabel('Сумма счета')
# plt.ylabel('Плотность')
# plt.grid(alpha=0.3)
# plt.show()



# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import numpy as np

# tips= sns.load_dataset("tips")
# print(tips.head())
#
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14,10))
#
# sns.histplot(data=tips, x='total_bill', ax=axes[0,0], color='skyblue')
# axes[0,0].set_title('Гистограмма счетов')
#
# sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0,1])
# axes[0,1].set_title('Ящики по дням')
#
# sns.scatterplot(data=tips, x='total_bill', y='tip',hue='smoker', ax=axes[1,0])
# axes[1,0].set_title('Рассеивание: счет vs чаевых')
#
# sns.barplot(data=tips, x='day', y='total_bill', ax=axes[1,1])
# axes[1,1].set_title('Средний счет по дням')
#
# plt.show()

# df = pd.DataFrame({
#     'sales': np.random.normal(100, 20, 200),
#     "region": np.random.choice(['Север','Юг', 'Восток','Запад'],200),
#     'month': np.random.choice(['Январь', 'Февраль','Март','Апрель'], 200),
#
# })
#
# print(df)
#
# fig, ax = plt.subplots(1,3,figsize=(15,5))
# sns.histplot(df['sales'], ax=ax[0], color='green')
# ax[0].set_title('Распределение продаж')
#
# sns.boxplot(data=df, x='region', y='sales', ax=ax[1])
# ax[1].set_title('Продажи по регионам')
#
# sns.barplot(data=df, x='month', y='sales', ax=ax[2],estimator=np.sum)
# ax[2].set_title('Суммарные продажи по месяцам')
# plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import numpy as np
#
# n_rows = 1000
# data_marketing = pd.DataFrame({
#     'Source': np.random.choice(['Google Ads', 'Target Ads', 'Influenxers'], n_rows, p=[0.5,0.3,0.2]),
#     'Lifetime_Months':np.random.geometric(p=0.25, size=n_rows)
# })
# print(data_marketing)
# data_marketing['Life_Months'] = data_marketing['Lifetime_Months'].clip(upper=12)
#
# plt.figure(figsize=(10,5))
# sns.set_theme(style='whitegrid')
#
# sns.kdeplot(data=data_marketing, x ='Lifetime_Months', hue='Source', fill=True, alpha=0.4, linewidth=2, palette='muted')
# plt.title('Как быстро уход клиенты в зав-ти от рекламного источника')
# plt.xlabel('Месяцы с момента первой покупки')
# plt.ylabel('Плотность (доля клиентов)')
# plt.xlim(1,12)
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import numpy as np
#
# days=['Пн', 'Вт','Ср','Чт','Пт','Сб','Вс']
# hours = [f'{h:02d}:00' for h in range(8,23)]
# grid = []
#
# for day in days:
#     for hour in hours:
#         base_order = np.random.randint(20,60)
#         if day in ['Пт','Сб'] and int(hour[:2]) >= 18:
#             base_order += 80
#         if day in ['Сб','Вс'] and 12 <= int(hour[:2]) <= 15:
#             base_order += 60
#
#         grid.append({'Day':day,'Hour':hour,'Order': base_order})
#
# df_orders = pd.DataFrame(grid)
#
# pivot_orders = df_orders.pivot(index='Day', columns='Hour', values='Order').reindex(days)
# print(pivot_orders)
#
# plt.figure(figsize=(12,15))
#
# sns.heatmap(pivot_orders, annot=True, cmap='YlOrRd', fmt='d', linewidths=.5, cbar_kws={'label':" Количество заказов"})
# plt.title('Почасовая интенсивность заказов в течении недели', fontsize=14, pad=15)
# plt.xlabel('Час суток', fontsize=12)
# plt.ylabel('День недели', fontsize=12)
#
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import numpy as np
#
#
# n_users = 400
# data_ab = pd.DataFrame({
#     'Group':np.random.choice(['A(Старый)', 'В (Новый)'], n_users, p=[0.5,0.5]),
#     'OS':np.random.choice(['IOS', 'Android'], n_users, p=[0.4,0.6]),
#     'SessionDuration': np.random.normal(loc=12, scale=4, size=n_users),
# })
# data_ab.loc[data_ab['Group'] == 'В (Новый)', 'SessionDuration'] += 2.5
#
# plt.figure(figsize=(10,6))
# sns.violinplot(data=data_ab, x='Group', y='SessionDuration', hue='OS', split=True, inner='quart', palette='muted')
#
# plt.title('Результаты A/B теста: Длительность сессии по группам и ОС', fontsize=14, pad=10)
# plt.grid()
# plt.xlabel('Группа теста')
# plt.ylabel('Длительность сессии в минутах')
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import numpy as np
#
# n_borrowers = 2000
# jobs = ['Freelance', 'State Employee', 'Corporate', 'Business Owner']
# df_credit = pd.DataFrame({
#     'Employment': np.random.choice(jobs, n_borrowers, p=[0.2, 0.3, 0.4, 0.1]),
#     'Credit_Score': np.random.normal(loc=650 , scale=70, size=n_borrowers),
# })
#
# df_credit.loc[df_credit['Employment'] == 'Corporate','Credit_Score' ] += 45
# df_credit.loc[df_credit['Employment'] == 'Freelance','Credit_Score' ] -= 30
# df_credit['Credit_Score'] = df_credit['Credit_Score'].clip(300,850)
#
# print(df_credit.head())
#
# plt.figure(figsize=(10,6))
#
# sns.boxenplot(data=df_credit, x='Employment', y='Credit_Score', palette='coolwarm', hue='Employment')
# plt.title('Распределение кредитного рейтинга заемщиков по типам занятости')
# plt.xlabel('Тип занятости')
# plt.ylabel('Кредитный рейтинг')
# plt.show()


#---------------------------------------------------
#31.10 plotly
#
# import plotly.express as px
# from plotly.graph_objs.layout.geo import projection

# data = {
#     'Месяц': ['Ян', 'Фев', 'Мар', 'Апр'],
#     'Температура': [-5,-3,2,10]
# }
#
# fig = px.line(data, x='Месяц', y='Температура', title='средняя температура')
# fig.write_html('Температура.html')
# fig.write_image('Температура.png')
# # fig.show()
#
# data = {
#     'Категория': ['Продукты', 'Транспорт', 'Развлечения'],
#     'Расходы': [5000,3000, 2000]
#
# }
#
# fig = px.bar(data, x= 'Категория', y='Расходы', title='Расходы за месяц', color='Категория', color_discrete_map={'Продукты': 'orange', 'Транспорт':'green', 'Развлечения':'yellow'})
# fig.update_traces(textposition='outside', texttemplate='%{y} Руб')
# fig.show()


# fig = px.funnel_area(names=['A', 'B', 'C'], values=[10,20,30], title='Площадь воронки')
# fig.show()

# df = px.data.iris()
#
# # fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title='Точечный график')
# # fig = px.scatter_3d(df, x="sepal_width", y="sepal_length",z='petal_length' ,color="species", title='3D Точечный график')
# # fig = px.scatter_polar(df, r="sepal_length", theta='sepal_width', color="species", title='Полярный график')
# fig = px.scatter_ternary(df, a="sepal_length", b='sepal_width',c='petal_length', color="species", title='Тернарный график')
# fig.show()
#
#
# df = px.data.gapminder()
# fig = px.scatter_geo(df, locations='iso_alpha', color='continent',hover_name='country',size='pop', projection='natural earth',title='Географический график' )
#
# fig.show()



# df = px.data.gapminder()
# fig = px.bar_polar(df, r='pop', theta='continent',color='continent',title='Полярный столбчатый гарфик' )
# fig.show()


# df = px.data.gapminder()
# fig = px.box(df, x='continent',y= 'lifeExp', color='continent',title='Коробчатый график' )
# fig.show()

#
# df = px.data.gapminder()
#
# selected_year = 2007
# df_year = df[df['year'] == selected_year]
# df_continent = df_year.groupby(['continent']).agg({'pop': 'sum'}).reset_index()
# df_continent['percentage'] = (df_continent['pop'] / df_continent['pop'].sum()) * 100
#
# fig = px.pie(df_continent, values='pop', names='continent', title=f'Распределение населения по континентам в {selected_year}году', color='continent', color_discrete_sequence=px.colors.qualitative.Set3, hole=0.4, labels={'continent': 'Континент', 'pop':'Население'})
# fig.update_traces(textposition='inside', textinfo='percent + label')
# fig.update_layout(showlegend=True, legend_title_text='Континент', margin=dict(l=20, r=20, t=80, b=20))
#
# fig.show()
#


# df = px.data.gapminder()
# fig = px.sunburst(df, path=['continent', 'country'], values='pop', title='Круговая иерархия')
# fig.show()
#
# df = px.data.gapminder()
# selected_year = 2007
# df_year = df[df['year'] == selected_year]
#
# print(df_year.head())
#
# fig = px.treemap(df_year,path=['continent', 'country'], values='pop', color='lifeExp', hover_data=['gdpPercap'], color_continuous_scale='RDbU', title=f'Иеррхическое дерево по странам и континентам в {selected_year} году')
# fig.update_layout(margin=dict(t=50, r=25, l=25, b=25))
# fig.show()
#
#
# df = px.data.gapminder().query('year == 2007')
#
# fig= px.choropleth(df, locations='iso_alpha', color='gdpPercap', hover_name='country', color_continuous_scale=px.colors.sequential.YlOrRd )
#
# fig.update_layout(title='world GPA per Capite (2007)', geo_scope='world')
# fig.show()
# fig.show()


#временная шкала диаграмма Ганта
# import plotly.express as px
# import pandas as pd
# from plotly.graph_objs.layout.scene import xaxis

# data = {
#     'Event': [
#         'Начало второй мировой войны',
#         'Распад СССР',
#         'Первый человек в космосе',
#         'Создание интернета',
#         'Введение евро',
#         'Начало COVID-19 пандемии',
#         'Разработка вакцин против COVID-19'
#     ],
#     'Start': [
#         '1939-09-01',
#         '1990-03-11',
#         '1961-04-12',
#         '1983-01-01',
#         '1999-01-01',
#         '2020-01-01',
#         '2020-12-01'
#     ],
#     'End': [
#         '1945-09-02',
#         '1991-12-25',
#         '1969-07-24',
#         '1990-01-01',
#         '1999-01-01',
#         '2023-01-01',
#         '2021-12-31',
#     ],
#     'Category': [
#         'Война',
#         'Политика',
#         'Космос',
#         'Технологии',
#         'Экономика',
#         'Здоровье',
#         'Здоровье'
#     ],
#     'Description': [
#         'Второй мировой конфликт, начавшийся с нападения Германии на Польшу',
#         'Событие, символирующее конец Хлоддной войны',
#         'Нил Амстронг стал первым человеком ступившим на Луну',
#         'Начало разработки глобальной сети свяязи',
#         'Введение единой валюты во многих европейских странах',
#         'Глобальная пандемия, вызванная вирусом',
#         'Создание и внедрение вакцин для борьбы с COVID-19'
#     ]
#
# }
# df = pd.DataFrame(data)
#
# df['Start'] = pd.to_datetime(df['Start'])
# df['End'] = pd.to_datetime(df['End'])
#
# fig = px.timeline(df, x_start='Start', x_end='End', y='Event', color='Category', title='Временная шкала ключевых исторических событий', labels={'Event':'Cобытия', 'Category':'Категория'}, hover_data={'Description': True, 'Start':False, 'End':False})
#
# fig.update_yaxes(autorange='reversed') #разворот сверху вниз ось y
# fig.update_layout(bargap=0.12, xaxis_title='Дата', margin={'l':200, 'r':50, 'b':0, 't':100}) # отступы между горизонтальными полосами событий
#
#
#
# fig.show()



#-------01.11


import plotly.express as px

df = px.data.gapminder()

fig = px.bar(df, x='continent', y='pop',animation_frame='year', color='continent',title='Население по контнентам')

fig.show()
# fig.write_html('animated_chart.html')




# df = px.data.gapminder()
# fig = px.scatter_geo(df, locations='iso_alpha', projection='orthographic', color='continent', hover_name='country', size='pop') #аннимаци карта -> глобус
#
# fig.show()


#-------Дашборды
from dash import Dash, html

