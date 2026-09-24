# a = int(input("Введите кол-во символов:" ))
# b = input("Введите символ:" )
# c = int(input("Введите ориентацию, где 0 - горизонтальная, 1 - вертикальная: "))
# i = 0
# while i < a:
#     if c == 0:
#         print(b, end=' ')
#     if c == 1:
#         print(b)
#     i += 1

# поиск числа в кубе

def cube(a):
    return a**3

for i in range(1, 11):
    print(i, "в кубе= ", cube(i))

