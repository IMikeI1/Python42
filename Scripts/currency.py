import requests
from bs4 import BeautifulSoup as BS
from requests.exceptions import ConnectionError
import json
def get_HTML(url: str) -> str|None:
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200 and str(status)[0] != 3:  # 404,503,301
            # print(f'Ошибка запроса. Код ответа - {status}')
            return None
            print(f"Код ответа - {status}")
        html = response.text
    except Exception as error:
        print('Нет ответа от сервера')
        print(error)
        return None
def parse_HTML(html: str):
    soup: BS = BS(html, "html.parser")
    current_date = (soup.find("h2", class_="h2 blue").text.split("\n")[-1].strip()[:10])
    table = soup.find("div", class_="module-tableSort")
    rows = table.find_all('tr')[2:]
    for row in rows:
        if not row.find('td', class_='t-center'):
            continue
            code = row.find('td', class_='t-center').text
            number_code = code.split()[0]
            txt_code = code.split()[1]
        name = row.find('td', class_='t-left').text
        value = row.find('td', class_='t-right').text
        print(f'{code} {name} {value}')
        name = row.find('td', class_='t-left').text.split('\n')[0]
        value = row.find('td', class_='t-right').text.split()
        print(print(f'{number_code}-{txt_code} {name} {value}'))

        courses[current_date][txt_code] = {
           " number_code": number_code,
            "name": name,
            "value": value
        }
        return courses
def write_date_to_json(data: dict) -> None
    with open('cor')

        pass



url = "https://www.alta.ru/currency/"
html = get_HTML(url)
if html:
    parse_HTML(html)
# почитать про статус-код (400 - ошибки на стороне клиента, 500 - ошибки на стороне сервера)