import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

service = Service(
    executable_path="/home/laziz/PycharmProjects/practice-with-the-api/parsing_selenium/"
                    "part_2/lesson_4/chromedriver"
)

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                     " Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36")

options.add_argument("--disable-blink-features=AutomationControlled")

options.headless = True
driver = webdriver.Chrome(service=service, options=options)


url = "https://www.avito.ru/all/tovary_dlya_kompyutera/komplektuyuschie/videokarty" \
      "-ASgBAgICAkTGB~pm7gmmZw?cd=1"

try:
    driver.get(url=url)
    # print(driver.window_handles)
    print(f'URL: {driver.current_url}')
    print("-" * 100)
    # time.sleep(2)
    # driver.implicitly_wait(10)
    items = driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")

    items[0].click()
    # print(driver.window_handles)
    # time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(2)
    print(f'URL: {driver.current_url}')
    print("-" * 100)

    username = driver.find_element(By.CLASS_NAME, 'style-seller-info-name-uWwYv')
    print(f"User name: {username.text}")
    print("-" * 100)
    # time.sleep(2)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(3)
    print(f'URL: {driver.current_url}')
    print("-" * 100)

    items[1].click()
    # time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(2)
    print(f'URL: {driver.current_url}')
    print("-" * 100)
    username = driver.find_element(By.CLASS_NAME, "styles-module-size_ms-EVWML")
    print(f"User name: {username.text}")
    print("-" * 100)
    data_pub = driver.find_element(By.XPATH, "//span[@data-marker='item-view/item-date']")
    print(f"Date: {data_pub.text}")
    print("-" * 100)
    register_date = driver.find_elements(By.CLASS_NAME, 'style-seller-info-value-vOioL')
    for i in register_date[1:]:
        print(f"User sience: {i.text}")

    print("#" * 100)
    # time.sleep(3)
except Exception as ex:
    print(ex)
finally:

    driver.close()
    driver.quit()