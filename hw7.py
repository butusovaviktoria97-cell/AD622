math = {"Матвей","Евгения","Михаил","Максим","Наталья"}
physics = {"Максим", "Матвей", "Александр"}
all_win = math|physics
print("Все призеры: ",list(all_win))
win_two = math & physics
print("Призеры обеих олимпиад: ", win_two)
math_new = math & physics
print("Обновленный список призеров по математике: ",math_new)