def hello():
    print('Hello')

def bye():
    print("Bye")

def print_name(name):
    print(name)
  # сигнатура имя функций
def print_info(name, lastname, age, city):
    info = {
        'name': name,
        'lastname': lastname,
        'age' : age,
        'city' : city

    }
    print(info)

    user_name = "Dmitry"
    user_lastname = "Ivanov"
    user_age = 32
    user_city = "Moscow"
    # именованные аргументы
    print_info(name=user_name, age=user_age, lastname=user_lastname, city=user_city)

# позиционные аргументы
    print_info(user_name, user_age, user_city, user_lastname)
# комбинированный способ ()



# name = 'Masha'
# last_name = 'Dima'
# print_name()