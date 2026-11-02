# import matplotlib.pyplot as plt
# import numpy as np
# Задача 1: продажи отделов магазина (Настройка цветов и сетки)
# Условие: Магазин продает три категории товаров:
# Электроника, Одежда и Книги. Данные разбиты по кварталам.
# Постройте график, задайте категории вручную с помощью списка
# цветов (colors) и включите фоновую сетку для удобства чтения.

# quarters = ['Q1', 'Q2', 'Q3', 'Q4']
# electronics = [40, 55, 48, 70]
# clothing = [30, 45, 40, 65]
# books = [15, 20, 18, 25]
#
# x = np.arange(len(quarters)) # [0, 1, 2, 3]
#
# plt.figure(figsize=(10, 6))
#
# colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
#
# plt.bar(x, electronics, color=colors[0], label='Электроника', edgecolor='black', alpha=0.5)
# plt.bar(x, clothing, color=colors[1], label='Одежда', edgecolor='black', alpha=0.5)
# plt.bar(x, books, color=colors[2], label='Книги', edgecolor='black', alpha=0.5)
#
# plt.xlabel('Кварталы', fontsize=12)
# plt.ylabel('Объем продаж (тыс. руб.)', fontsize=12)
# plt.title('Динамика продаж отделов магазина за год', fontsize=14, fontweight='bold')
# plt.xticks(ticks=x, labels=quarters)
#
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.legend(loc='upper left')
#
# plt.ylim(0, 80)
# plt.tight_layout()
#
# plt.show()


# Задача 2: круговая диаграмма (Доли рынка смартфонов)
# Условие: У вас есть данные о долях рынка четырех популярных брендов смартфонов: Apple, Samsung, Xiaomi и Другие. Постройте простую круговую диаграмму, добавьте подписи к каждому сектору и выведите проценты внутри графика с округлением до одного знака после запятой.
#
# Данные: названия и их доли в процентах:
# •	brands = ['Apple', 'Samsung', 'Xiaomi', 'Другие']
# •	market_share = [30, 25, 20, 25]

import matplotlib.pyplot as plt

brands = ['Apple', 'Samsung', 'Xiaomi', 'Другие']
market_share = [30, 25, 20, 25]

plt.figure(figsize=(7, 5))

plt.pie(
    market_share,
    labels=brands,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 11}
)

plt.axis('equal')
plt.title('Доли рынка смартфонов(%)', fontsize=14, fontweight='bold')

plt.show()