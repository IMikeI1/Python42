import requests
from bs4 import BeautifulSoup as Bs


def get_html(url: str) -> str:
    responses = requests.get(url)
    status = responses.status_code
    print(f" код ответ - {status}")
    html = responses.text
    return html

def parse_html(html: str):
    soup: Bs = Bs(html, 'html.parser')

    pass


URL = "https://www.alta.ru/currency/"
html = get_html(URL)
parse_html(html)