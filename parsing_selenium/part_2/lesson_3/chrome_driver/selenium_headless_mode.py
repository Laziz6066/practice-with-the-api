import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import pickle
from parsing_selenium.part_2.lesson_1.chrome_driver.auth_data import tel_number, password


service = Service(
    executable_path="/parsing_selenium/part_2/lesson_1/chrome_driver/chromedriver"
)

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                     " Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36")

options.add_argument("--disable-blink-features=AutomationControlled")

options.headless = True
driver = webdriver.Chrome(service=service, options=options)


url = "https://vk.com/"

driver.get(url)

try:
    driver.get(url=url)
    time.sleep(1)
    email_element = driver.find_element(By.ID, 'index_email')
    email_element.clear()
    email_element.send_keys(tel_number)
    time.sleep(1)
    email_element.send_keys(Keys.ENTER)

    time.sleep(2)
    button = driver.find_element(By.CLASS_NAME,
                                 "vkc__PureButton__button.vkc__Link__link.vkc__Link__primary.vkc__Bottom__switchToPassword")

    button.click()
    time.sleep(2)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    time.sleep(2)
    video_link = driver.find_element(By.CLASS_NAME, 'LeftMenuItem-module__label--itYtZ')
    video_link.click()
    time.sleep(2)
    video_play = driver.find_element(By.CLASS_NAME, "VideoPreview")
    video_play.click()
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:

    driver.close()
    driver.quit()