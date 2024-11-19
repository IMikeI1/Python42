# def hello():
#     print('Hello')
#
# def bye():
#     print("Bye")
#
# def print_name(name):
#     print(name)
#   # сигнатура имя функций
# def print_info(name, lastname, age, city):
#     info = {
#         'name': name,
#         'lastname': lastname,
#         'age' : age,
#         'city' : city
#
#     }
#     print(info)
#
#     user_name = "Dmitry"
#     user_lastname = "Ivanov"
#     user_age = 32
#     user_city = "Moscow"
#     # именованные аргументы

# print_info(name=user_name, age=user_age, lastname=user_lastname, city=user_city)

def text_analyse(text):

    '''
    :param text = str
    :return: dict
    '''

    stat = {}
    for s in text:
        stat[s] = text.count(s)
    return stat
    # print(text_analyse(text="Hello"))

def text_to_list(text: str) -> list[str]:
    return text.split(', ')

# print(text_to_list(text="i love python"))


emails = [
    "admin@mail.ru",
    "alex@yandex.ru",
    "alena@mail.ru",
    "igor@mail.ru"

]

def get_emails(in_emails: list[str], domen: str = '.ru') -> list:
    emails = []
    for in email in




def check_age(age: int|str) -> bool:
    if isinstance(age)





# позиционные аргументы
    print_info(user_name, user_age, user_city, user_lastname)
# комбинированный способ ()



# name = 'Masha'
# last_name = 'Dima'
# print_name()