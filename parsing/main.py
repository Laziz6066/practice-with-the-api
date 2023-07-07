import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {
    "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
        "YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36"
}

for j in range(1, 8):
    sleep(1)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={j}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
    for i in data:
        name = i.find('h4', class_='card-title').text.replace('\n', '')
        price = i.find('h5').text.replace('\n', '')
        url_img = "https://scrapingclub.com" + i.find('img', class_='card-img-top img-fluid').get('src')

        print(f"{name} \n {price} \n {url_img} \n\n")
    j += 1