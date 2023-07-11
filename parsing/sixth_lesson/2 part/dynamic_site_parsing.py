import json
import os.path
import time
import requests

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36"
}


def get_data_file(headers):
    url = "https://www.landingfolio.com/"

    # r = requests.get(url=url, headers=headers)
    # with open("index.html", 'w') as file:
    #     file.write(r.text)

    offset = 0
    count = 0
    result_list = []

    while offset < 13:
        url = f"https://s3.landingfolio.com/inspiration?page={offset}&sortBy=free-first"
        response = requests.get(url=url, headers=headers)
        data = response.json()
        for item in data:
            if 'postDate' in item:
                images_list = []
                screenshots = item.get("screenshots", [])
                for screenshot in screenshots:
                    images = screenshot.get("images", {})
                    desktop_image = images.get("desktop")
                    images_list.append(f"https://landingfoliocom.imgix.net/{desktop_image}")
                # img_count += len(images)

                result_list.append(
                    {
                        "page": f'{offset}',
                        "count": f"{count}",
                        'title': item.get('title'),
                        'url': item.get('url'),
                        "images": images_list
                    }
                )
                count += 1
                # print(result_list)
                # print(item.get('title'))
                # print(item.get('url'))
                # print(f"{image} \n{'*' * 100}")

            else:

                return "Work finished"

        print(f'[+] Processed {offset}')
        offset += 1
    with open('result_list.json', 'w') as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)


def download_images(file_path):
    try:
        with open(file_path) as file:
            src = json.load(file)
    except Exception as ex:
        print(ex)
        return 'Check the file path'

    for item in src:
        item_name = item.get('title')
        item_imgs = item.get('images')
        item_count = item.get('count')

        if not os.path.exists(f'data/{item_name}'):
            os.mkdir(f'data/{item_name}')

        for img in item_imgs:
            r = requests.get(url=img)
            with open(f'data/{item_name}/{item_name}_{item_count}.png', 'wb') as file:
                file.write(r.content)
        print('[+] Download')
    return 'Work finished'


def main():
    start_time = time.time()
    # print(get_data_file(headers=headers))
    print(download_images('result_list.json'))
    finish_time = time.time() - start_time
    print(f'Worked time: {finish_time}')


if __name__ == '__main__':
    main()