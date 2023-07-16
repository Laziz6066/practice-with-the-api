from bs4 import BeautifulSoup
from requests import Session
from time import sleep


headers = {
    "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
        "YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36"
}
url = "https://quotes.toscrape.com/"

work = Session()
work.get(url=url, headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
site_token = soup.find('form').find('input').get('value')
data = {"csrf_token": site_token, "username": "noname", "password": "password"}

result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)

