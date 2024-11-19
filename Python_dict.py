# словарь определяется функцие dict или литералом {}
# словарь хранит данные в формате ключ: значения

mydict = dict()

person = {}
person_2 = {'name': 'Elena', 'age': 26}

# получение элемента словаря ИМЯ_СЛОВАРЯ[КЛЮЧ]
print(person_2['name'])

# добовление элемента в словаря ИМЯ_СЛОВАРЯ[КЛЮЧ]= ЗНАЧЕНИЕ
person_2['phone'] = '2345345363'
print(person_2)

person_2['age'] = 45
print(person_2)

print(len(person_2))
person_2['language'] = {'main': 'Russian', 'other': 'English'}
person_2['age'] = {'12235485654', '23245', '12355465'}

print(person_2)
person_2[100] = ['231556846658', '23154', '24325456']
print(person_2)

print(list(person_2.keys())[0])
print(list(person_2.values()))

for key, value in person_2.items():
    print(f"key - {key}, value - {person_2[key]}")

print(len(person_2))
print(person_2.get('ghhg', {}).get('hghdgf', {}))
age = person_2.pop('age')
print(age)
print(person_2)

del person_2[100]
print(person_2)
person_1 = person_2.copy()
print(id(person_1))
print(id(person_2))
person_2['NEW'] = 'NEW'
print(person_2)
print(person_1)
print(person_2.popitem())
print(person_2.popitem())
a = {}.fromkeys([1,2,3], ['a', 'b', 'c'])
print(a)



# x = 5
# y = 6
# x,y = y,x
#
# print(x)
# print(y)
#
# name, age = ('Sasha', 25)
# print(name)
# print(age)


