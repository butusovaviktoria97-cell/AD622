text = ("Ежевику для ежат\nПринесли два ежа. \nЕжевику еле-еле \nЕжата возле ели съели.")
print(text)
# print(text.title().count("Е"[0]))

s = text.split()
# print(s)
count = sum(1 for word in s if word[0].lower() == "е")

print(count)





