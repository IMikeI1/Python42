# def get_info(name, age=34):
#     print(name.title())
#     print(age)
#
# a = [1,2,3]
# b = [*a, 4,5,6]
# print(b)
#
# def print_scores(name, *args):
#     print(f"name - {name}")
#     print(args[0])
#     print(args[1])
#     for i in args:
#         print(i)
#
# print_scores('Dima', 26, 27, 56, 23, 67 )
#
# def func(*args, **kwargs):
#     print(args)
#     pass
# func(1,2,3,4,5)
# def func_2(a, b):
#     pass

def print_pet_names(owner, **kwargs):
    print(f'Владелец - {owner}')
    # for key, value in pets.items():
    #     print(f"{key} - {value}")
    #
    for key in kwargs.keys():
            print(f"{key} - {kwargs[key]}")

print_pet_names('Alex', dog='Tuzik', cat='Barsic')