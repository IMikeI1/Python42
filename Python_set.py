# множества set()
from pyhton_base import number

numbers = {1, 2, 2, 2, 2, 4, 5}
print(type(numbers))
print(numbers)

names = ['Sasha', 'Masha', 'Sasha', 'Masha']
names = list(set(names))
print(names)

# добовление элемента во множество

numbers.add(6)
print(numbers)

# удоление элемента из множества
numbers.remove(2)
print(numbers)

# удоление элемента из множества
numbers.discard(10)
print(numbers)

first_numbers = {1, 2, 3, 4, 5}
second_numbers = {4, 5, 6, 7, 8}

# объединение множества

third_numbers = first_numbers.union(second_numbers)
print(third_numbers)
print(first_numbers | )