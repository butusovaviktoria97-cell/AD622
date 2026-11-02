# дз через сиабон
import matplotlib.pyplot as plt
import seaborn as sns

# tips = sns.load_dataset("tips")
#
# plt.figure(figsize=(10,5))
#
# ax=sns.scatterplot( data=tips,x='total_bill',y='tip',hue='sex', palette='Set1',s=100, alpha=0.8)
# ax.set_title('Счет vs Чаевые', fontsize=14)
# ax.set_xlabel('Сумма счета')
# ax.set_ylabel('Чаевые')
#
# plt.grid(alpha=0.3)
# plt.tight_layout()
#
# plt.show()

# Задача 2: Ящик с усами (Распределение по категориям)
# Условие: Постройте график "ящик с усами" (boxplot),
# чтобы сравнить распределение общего счета (total_bill) между курящими (smoker)
# и некурящими клиентами. На основе датасета tips.

# tips = sns.load_dataset("tips")
#
# plt.figure(figsize=(10, 6))
#
# sns.boxplot(data=tips, x='smoker', y='total_bill', palette='Set2')
#
# plt.title('Распределение счета: курящие vs некурящие', fontsize=14, fontweight='bold')
# plt.xlabel('Курение', fontsize=12)
# plt.ylabel('Общий счет', fontsize=12)
#
# plt.xticks(ticks=[0, 1], labels=['Некурящие', 'Курящие'])
#
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.tight_layout()
#
# plt.show()


# Задача 3: Матрица корреляции и Тепловая карта (heatmap)
# Условие: Найдите корреляцию между всеми числовыми признаками
# в датасете iris и визуализируйте её в виде тепловой карты.
# Выведите коэффициенты корреляции внутри ячеек и используйте
# контрастную цветовую палитру (например, coolwarm).

iris = sns.load_dataset("iris")

corr_matrix = iris.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f",cmap="coolwarm", center=0, linewidths=.5, linecolor='white')
plt.title('Матрица корреляции признаков Iris', fontsize=14, fontweight='bold')
plt.tight_layout()

plt.show()