import time
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import random
from fake_useragent import UserAgent
from seleniumwire import webdriver


# proxy_options = {
#     'proxy': {
#         'https': f"http://{login}: {password}@138.128.91.65:8000"
#     }
# }
user_agents = [
    'hello_world',
    'python_today',
    'best_of_the_best'
]


useragent = UserAgent()

service = Service(
    executable_path="/home/laziz/PycharmProjects/practice-with-the-api/parsing_selenium"
                    "/part_1/lesson_2/chrome_driver/chromedriver"
)

options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={random.choice(user_agents)}")
options.add_argument(f"user-agent={useragent.random}")
# 84.54.71.56
# options.add_argument("--proxy-server=138.128.91.65:8000")
driver = webdriver.Chrome(service=service, options=options)

url = "https://whatmyuseragent.com/"


driver.get(url)

try:
    # driver.get(url=url)
    # time.sleep(5)
    # driver.get('https://stackoverflow.com/')
    # time.sleep(5)
    # driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.get('https://stackoverflow.com/')
    # time.sleep(5)
    # driver.save_screenshot('2.png')
    driver.get('https://2ip.ru')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()