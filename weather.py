import json
from textwrap import indent

import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent

def get_html(url: str) -> str | None:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    # headers = {"User-Agent": UserAgent().random}
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200 or str(response.status_code)[0] == "3":
            html = response.text
            # with open("index_1.html", "w") as file:
            #     file.write(html)
            return  html
        else:
            print(f"Ошибка запроса. Код ответа: {response.status_code}")
            return None
    except ConnectionError as err:
        print(f"Ошибка запроса.\n{err}")
        return None

def get_weather_from_day(html: str) -> dict:
    soup = Bs(html, "html.parser")
    weather_info = {}
    day = soup.find("div", "dates short-d").text
    weather_info[day] = {}
    table = soup.find("div", class_="weather-short").find("table")
    table_rows = table.find_all("tr")
    for row in table_rows:

        weather_day = row.find("td", class_="weather-day").text
        weather_info[day][weather_day] = {}

        weather_temperature = row.find("td", class_="weather-temperature").text
        weather_type = row.find("div", class_="wi")["title"]
        weather_feeling = row.find("td", class_="weather-feeling").text
        weather_probability = row.find("td", class_="weather-probability").text

        weather_info[day][weather_day]["weather-temperature"] = weather_temperature
        weather_info[day][weather_day]["weather-type"] = weather_type
        weather_info[day][weather_day]["weather-feeling"] = weather_feeling
        weather_info[day][weather_day]["weather-probability"] = weather_probability
    return weather_info

def write_data_to_json(data: dict) -> None:
    with open("weather.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
html = get_html(url=URL)
if html:
    data=get_weather_from_day(html)
    write_data_to_json(data)


