import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

service = Service(
    executable_path="/parsing_selenium/part_2/lesson_1/chrome_driver/chromedriver"
)

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                     " Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36")

options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(service=service, options=options)


url = "https://www.avito.ru/all/tovary_dlya_kompyutera/komplektuyuschie/videokarty" \
      "-ASgBAgICAkTGB~pm7gmmZw?cd=1"

driver.get(url)

try:
    driver.get(url=url)
    items = driver.find_element()
except Exception as ex:
    print(ex)
finally:

    driver.close()
    driver.quit()