import random
from time import sleep
from bs4 import BeautifulSoup
import requests
import json
import csv

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 " \
                        "(KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.575 " \
                        "(beta) Yowser/2.5 Safari/537.36"}
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
# req = requests.get(url, headers=headers)

# src = req.text


# with open('index.html', 'w') as file:
#     file.write(src)

# with open('index.html') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
#
# all_categoreis = {}
# for i in all_products_hrefs:
#     item_text = i.text
#     item_href = 'https://health-diet.ru' + i.get('href')
#     all_categoreis[item_text] = item_href
#
# with open('all_categories.json', 'w') as file:
#     json.dump(all_categoreis, file, indent=4, ensure_ascii=False)


with open('all_categories.json') as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
count = 0
print(f"Всего тиераций: {iteration_count}")
for category_name, category_href in all_categories.items():

    rep = [',', '.', '-', ' ', "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", 'w') as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbon = table_head[4].text

    with open(f'data/{count}_{category_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbon
            )
        )

    products_data = soup.find(class_="mzr-tc-group-table").find('tbody').find_all('tr')

    product_info = []

    for item in products_data:
        products_tds = item.find_all('td')
        title = products_tds[0].find('a').text
        calories = products_tds[1].text
        proteins = products_tds[1].text
        fats = products_tds[1].text
        carbon = products_tds[1].text

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbon": carbon
            }
        )
        with open(f'data/{count}_{category_name}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbon
                )
            )

    with open(f'data/{count}_{category_name}.json', 'a', encoding='utf-8') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)
    count += 1
    print(f"Итерация {count} {category_name} записан...")
    iteration_count -= 1
    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"Осталось итераций: {iteration_count}")
    sleep(random.randint(2, 4))
