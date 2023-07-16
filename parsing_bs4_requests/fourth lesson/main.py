import json
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_data():
    headers = {

        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36"
    }
    # title_and_hrefs = {}
    # all_hotels_hrefs = []
    # for i in range(0, 100, 20):
    #     url = f'https://tury.ru/hotel/?cn=0&ct=0&cat=1317&txt_geo=&srch=&s={i}'
    #     req = requests.get(url, headers)
    #
    #     soup = BeautifulSoup(req.text, 'lxml')
    #     all_hotels = soup.find_all('div', class_='reviews-travel__item')
    #
    #     for i in all_hotels:
    #         hotel_name = i.find('div', class_='h4').text
    #         hotel_href = i.find('a').get('href')
    #         print(hotel_name, ':', hotel_href)
    #         all_hotels_hrefs.append(hotel_href)
    #         title_and_hrefs[hotel_name] = hotel_href
    #
    # with open('data/title_and_links.json', 'w') as file:
    #     json.dump(title_and_hrefs, file, indent=4, ensure_ascii=False)

#     with open('title_and_links.json') as file:
#         title_link = json.load(file)
#     count = 0
#     for hotel_name, hotel_href in title_link.items():
#
#         rep = ['*', ' ']
#         for item in rep:
#             if item in hotel_name:
#                 hotel_name = hotel_name.replace(item, '_')
#
#         req = requests.get(url=hotel_href, headers=headers)
#         src = req.text
#
#         with open(f'data/{count}_{hotel_name}.html', 'w') as file:
#             file.write(src)
#
#         with open(f'data/{count}_{hotel_name}.html') as file:
#             src = file.read()
#
#         soup = BeautifulSoup(src, 'lxml')
#         short_description = soup.find('div', class_='hotel__text')
#         for i in short_description:
#             hotel_description = i.text.strip()
#         full_description = soup.find_all('ul', class_='about-hotel-list')
#
#         print(full_description)
#         count += 1
#         if count > 1:
#             break
#
#
# get_data()


def get_data_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                                                         "(KHTML, like Gecko)Chrome/112.0.0.0 YaBrowser/"
                                                         "23.5.1.575 (beta) Yowser/2.5 Safari/537.36")

    try:
        driver = webdriver.Firefox(executable_path="/parsing_bs4_requests/fourth lesson/geckodriver",
                                   options=options)
        driver.get(url=url)
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
