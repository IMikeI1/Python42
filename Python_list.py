# Создание списка
# с использованием функцие list()
from itertools import count

list()
# с использованием литерала []
#             0    1 (-2) 2 (-1)
# доступ к элементам списка
user_2 = ['Dima', 'Vova', 'Elena']
print(user_2[0])
print(user_2[-1])
print(user_2[1])

# добовление элемента в список
user_2.append('Olga')

# расширение списка элементами другого списка
user_2 +=['Sasha', 'Masha']
user_2.extend(['Natasha' "Sveta"])
# добовление элемента в произвольное место
user_2.insert(0, 'Zero')
user_2.insert(-1, 'Last')
user_2.insert(len(user_2), 'Last !!!')
print(user_2)

# получение количество элементов списка

print(len(user_2))

# pop - удалить элемент и получить его
user_2.pop(0)

# count - подсчет кол-во элементов в списке

print(user_2.count('Sasha'))
# user_2.remove('Sasha')(первого, которого он нашел)
print(user_2)

# получение индекса элемента по его значению(первого, которого нашел)
print(user_2.index('Sasha', 5, 11))

# user_2.clear()
user_3 = [1, 2, 3, 4]
print(user_2 + user_3)

# win



