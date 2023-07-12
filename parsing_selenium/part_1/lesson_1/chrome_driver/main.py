import time

from selenium import webdriver


from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/parsing_selenium/part_1/lesson_1/chrome_driver/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.instagram.com/"


driver.get(url)

try:
    driver.get(url=url)
    time.sleep(5)
    # driver.get('https://stackoverflow.com/')
    # time.sleep(5)
    # driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.get('https://stackoverflow.com/')
    # time.sleep(5)
    # driver.save_screenshot('2.png')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()