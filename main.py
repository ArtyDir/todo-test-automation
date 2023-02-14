import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://time.is')

for i in range(0, 5):
    clock = driver.find_element(By.XPATH, "//time[@id='clock']")
    print(clock.text)
    driver.save_screenshot(f'{i}.png')
    time.sleep(1)

driver.close()
