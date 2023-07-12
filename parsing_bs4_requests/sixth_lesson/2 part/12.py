import requests


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36"
}
offset = 0
url = f"https://s3.landingfolio.com/inspiration?page={offset}&sortBy=free-first"
response = requests.get(url=url, headers=headers)
data = response.json()

for item in data:
    if len(item['postDate']) > 2:
        print(f'{item["title"]}')
        print(offset)
    else:
        print('n')
    offset += 1