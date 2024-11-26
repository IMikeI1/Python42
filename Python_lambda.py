from functools import reduce
# def sum_number(a, b):
#     return a + b
# result = sum_number(5, 4)
# print(result)
# double = lambda x: x**2
# print(double(2))
def double(x str)->int:
    if x.isdigital():
    return x**(x)2
#


list_of_numbers = ['1', '234', '234', '22', '11']
sum_numbers = reduce(lambda x,y: int(x)+int(y), list_of_numbers)
print(reduce(lambda x,y: x+y, list_of_numbers))
#
# list_int_numbers = []
#
# list_double_numbers = list(map(lambda x: int(x)**2, list_of_numbers))


# for i in list_of_numbers:
#     if i.isdigit():
#       list_int_numbers.append(int(i))


# users = [['alex', 70], ['dima', 50], ['elena', 30], ['sveta', 25]]



