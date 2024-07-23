# в данных примерах библиотека matplotlib позволяет визуализировать данные
# в форме столбчатой диаграммы и линейных графиков

import matplotlib.pyplot as plt

x = [0, 5, 4, 4, 5, 6, 6, 7, 6, 7, 7, 5, 2, 1, 1, 0]
y = [3, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 0, 0, 1, 2, 3]

plt.xlabel('Ось x')
plt.ylabel('Ось y')

plt.plot(x, y, color='blue', marker='o', markersize=7)
plt.show()

x = ['Апрель', 'Май', 'Июнь', 'Июль']
y = [1, 2, 3, 6]

plt.bar(x, y, label='Уровень сложности обучения в Urban')
plt.xlabel('Месяц года')
plt.ylabel('Сложность, в мес.')
plt.legend()
plt.show()