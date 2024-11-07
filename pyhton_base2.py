# условное выражение
from pyhton_base import number

age = 14
if age < 20:
    print('Error')
    print('Error')
    if age < 15:
        print('Fatal')
    else:
        print('not fatal')
    elif age < 25:

    print('<25')
else:
    print('OK')
    print('Next')
    # цикл FOR

    number = [1,2,3,4,5,6,7,8,9]
    cars = ['bmw', 'audi', 'lada']
    N = 10
    # for i in range(N, 0, -1):
    #     print(i)
    #
    #     for car in cars:
    #         print(car)
    # for ind in range (len(cars)):
    #     print(ind, cars[ind])
a = 10

while a < 20:
    print(a)
    a += 1
    if a == 15:
        break


