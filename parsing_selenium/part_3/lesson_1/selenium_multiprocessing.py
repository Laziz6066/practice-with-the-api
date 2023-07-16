import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool


urls = ["https://stackoverflow.com", "https://www.instagram.com", "https://vk.com"]


def get_data(url):
    try:
        service = Service(
            executable_path="/home/laziz/PycharmProjects/practice-with-the-api/parsing_selenium/"
                            "part_3/lesson_1/chromedriver"
        )

        options = webdriver.ChromeOptions()

        options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                             " Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url=url)
        time.sleep(3)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    p = Pool(processes=2)
    p.map(get_data, urls)