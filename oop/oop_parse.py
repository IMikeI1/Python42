import requests
from bs4 import BeautifulSoup as Bs
import json


class Parser:
    def __init__(self, url):
        self.url = url
        self.data_weather = ()
        self.data_vacancies = []

    def get_html(self):
        response = requests.get(self.url)
        self.html = response.text


    def parse_html(self, html):
        self.get_html()
        soup = Bs(html, "parse_html")
        data = soup.find_all("table", class_="weather" )
        self.data_weather = {"data": data}

    def write_data_to_file(self):
        with open("file.txt", "w") as f:
            json.dump(self.data_weather, f, indent=2)


parser_weather =Parser(url="weather.com")
parser_weather.parse_html()

