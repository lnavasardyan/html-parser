import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_url():
    for count in range(1, 7):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        data = soup.find_all("div", class_="w-full rounded border")

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url


# Список для хранения данных
items = []

for card_url in get_url():
    response = requests.get(card_url).text
    soup = BeautifulSoup(response, 'lxml')
    data = soup.find("div", class_="my-8 w-full rounded border")

    name = data.find("h3", class_="card-title").text.strip()
    price = data.find("h4", class_="my-4 card-price").text.strip()
    description = data.find("p", class_="card-description").text.strip()
    url_img = "https://scrapingclub.com" + data.find("img").get("src")

    # Добавляем данные в список
    items.append({
        "Название": name,
        "Цена": price,
        "Описание": description,
        "Ссылка на изображение": url_img
    })

# Создание Excel-файла
df = pd.DataFrame(items)
df.to_excel("products.xlsx", index=False)

print("✅ Данные успешно сохранены в файл products.xlsx")







