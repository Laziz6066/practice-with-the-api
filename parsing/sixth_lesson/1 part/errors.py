import time

import requests
from bs4 import BeautifulSoup


def test_request(url, retry=5):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36"
    }

    try:
        response = requests.get(url=url, headers=headers)
        print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        time.sleep(3)
        if retry:
            print(f'[INFO] retry={retry} => {url}')
            return test_request(url, retry=(retry - 1))

        else:
            raise
    else:
        return response


def main():
    with open('links.txt') as file:
        urls = file.read().splitlines()
    for i in urls:
        try:
            r = test_request(i)
            soup = BeautifulSoup(r.text, 'lxml')
            print(f'{soup.title.text}\n{"-" * 100}')
        except Exception as ex:
            continue

if __name__ == "__main__":
    main()
