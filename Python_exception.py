from http.client import responses

import requests
"""
try:
блок,
где врозможна ошибка
except:
действие в случае
ошибке
finally:
блок кода,
котором выполнится в любом случае

"""
from Python_dict import mydict


# age = input('Enter the age:')
#
# try:
#     if age < 18
#         print('error')
#     else:
#         print('ok')
# except:
#     if age.isdigit():
#         if int (age) < 18:
#             print('error')
#         else:
#             print('ok')
#         else:
#         print('не число')

# def send_data():
#     data = {'name': 'Alex', 'age': 26}
#     data = None
#     return Exception('Error')
#
# # def get_data_from_server():
# # try:
# #     data = send_data()
# #     print(data)
# # except:
# #     data = []
# #     for i in data:
# #         print(i)
#
# try:
#     mydict = {'name': 'dima'}
#     if not mydict.get('age'):
#         print(mydict.get('age'))
#         raise Exception('Такого ключа нет!!!')
#
# except Exception as err
#     print(err)
#
# def check_age(age):
#     if age > 102:
#         raise Exception('Возраст слишком большой')
#     return age

# HTTP
def get_page(url):
   try:
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
   except:
       print("Error")
   finally:


url = "https://ru.wikipedia.org/wiki/%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D0%B8%D1%8F"
get_page(url)






