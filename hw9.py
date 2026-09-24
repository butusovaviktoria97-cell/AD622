import math

d = {

    'rectangle':lambda:print("Площадь прямоугольника размером 10*13:",10 * 13),
    'trapeze':lambda: print("Площадь трапеции для a=7, b=5, h=3:", (7+5)/2*3),
    'ring':lambda: print("Площадь окружности для r=2:", math.pi*2**2)
}

d['rectangle']()
d['trapeze']()
d['ring']()