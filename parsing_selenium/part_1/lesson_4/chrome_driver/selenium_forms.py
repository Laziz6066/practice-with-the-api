import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

service = Service(
    executable_path="/home/laziz/PycharmProjects/practice-with-the-api/parsing_selenium"
                    "/part_1/lesson_2/chrome_driver/chromedriver"
)

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                     " Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36")

driver = webdriver.Chrome(service=service, options=options)

url = "https://vk.com/"


driver.get(url)

try:
    driver.get(url=url)
    time.sleep(5)
    email_element = driver.find_element(By.ID, 'index_email')
    email_element.clear()
    email_element.send_keys('998906086066')
    time.sleep(3)
    login_button = driver.find_element(By.CLASS_NAME, 'FlatButton__content').click()
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:

    driver.close()
    driver.quit()