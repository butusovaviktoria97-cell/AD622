# напишите функции нахождения площади фигур:

import math

def s1(length, width):
    return length * width # площадь прямоугольника

def s2(base,height ):
    return 0.5 * base * height # площадь треугольника

def s3(radius):
    return math.pi * (radius**2)# площадь круга

a = int(input("Площадь какой фигуры необходимо найти? \n1 - прямоугольник \n2 - треугольник \n3 - "
              "круг. \nВведите номер фигуры: "))
if a == 1:
    b = float(input("Введите длину прямоугольника: "))
    c = float(input("Введите ширину прямоугольника: "))
    res = s1(b,c)
    print(res)
elif a == 2:
    b2 = float(input("Введите длину основания: "))
    h2 = float(input("Введите высоту треугольника: "))
    res = s2(b2,h2)
    print(res)
elif a == 3:
    r = float(input("Введите радиус окружности: "))
    res = s3(r)
    print(res)
else:
    print("Ошибка: введен неверный номер фигуры.")
