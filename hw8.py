def func(city):
    cou = 0

    def inner():
        nonlocal cou
        cou += 1
        print(city, cou)

    return inner


res1 = func("Москва")
res1()
res1()

res2 = func("Сочи")
res2()
res2()

res1()