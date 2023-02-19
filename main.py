import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://django-todo.org/')

# переход к начальной странице из тела сайта
body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()

time.sleep(3)

# переход к начальной странице из шапки сайта
head_elem = driver.find_element(By.XPATH, '//nav//a[@href="/login"]')
head_elem.click()

# ввод имени пользователя user1
username1_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
username1_elem.send_keys('user1')

# ввод пароля пользователя
password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# разлогинивание пользователя
logout = driver.find_element(By.XPATH, '//a[@href="/logout"]')
logout.click()

# ввод имени пользователя user2
body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()
username2_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
username2_elem.send_keys('user2')

# ввод пароля пользователя
password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# разлогинивание пользователя
logout = driver.find_element(By.XPATH, '//a[@href="/logout"]')
logout.click()

# ввод имени пользователя user3
body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()
username3_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
username3_elem.send_keys('user3')

# ввод пароля пользователя
password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# разлогинивание пользователя
logout = driver.find_element(By.XPATH, '//a[@href="/logout"]')
logout.click()

# ввод имени пользователя user4
body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()
username4_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
username4_elem.send_keys('user4')

# ввод пароля пользователя
password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# разлогинивание пользователя
logout = driver.find_element(By.XPATH, '//a[@href="/logout"]')
logout.click()

# ввод имени пользователя staffer
body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()
staffer_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
staffer_elem.send_keys('staffer')

# ввод пароля пользователя
password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# разлогинивание пользователя
logout = driver.find_element(By.XPATH, '//a[@href="/logout"]')
logout.click()

# ввод имени пользователя user1
body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()

username1_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
username1_elem.send_keys('user1')

# ввод пароля пользователя
password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# создание задачи пользователя user1 для user1
list = driver.find_element(By.XPATH, '//main/ul/li[1]/a')
list.click()

task = driver.find_element(By.XPATH, '//button[@id="AddTaskButton"]')
task.click()

task_title = driver.find_element(By.XPATH, '//input[@id="id_title"]')
task_title.send_keys('New task1_1')

description = driver.find_element(By.XPATH, '//textarea[@id="id_note"]')
description.send_keys('La-la-la')

date = driver.find_element(By.XPATH, '//input[@type="date"]')
date.send_keys('30.03.2023')

assigned_to = driver.find_element(By.XPATH, '//select[@name="assigned_to"]/option[text()="Tanya Stewart (user1)"]')
assigned_to.click()

submit = driver.find_element(By.XPATH, '//input[@name="add_edit_task"]')
submit.click()
driver.save_screenshot('screen_user1_1.png')

driver.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://django-todo.org/')

body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
body_elem.click()

username1_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
username1_elem.send_keys('user1')

password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
password_elem.send_keys('todo')

login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
login_button.click()

# создание задачи пользователя user1 для user2
list = driver.find_element(By.XPATH, '//main/ul/li[1]/a')
list.click()

task = driver.find_element(By.XPATH, '//button[@id="AddTaskButton"]')
task.click()

task_title = driver.find_element(By.XPATH, '//input[@id="id_title"]')
task_title.send_keys('New task1_2')

description = driver.find_element(By.XPATH, '//textarea[@id="id_note"]')
description.send_keys('La-la-la')

date = driver.find_element(By.XPATH, '//input[@type="date"]')
date.send_keys('30.03.2023')

assigned_to = driver.find_element(By.XPATH, '//select[@name="assigned_to"]/option[text()="Brittany Wright (user2)"]')
assigned_to.click()

submit = driver.find_element(By.XPATH, '//input[@name="add_edit_task"]')
submit.click()
driver.save_screenshot('screen_user1_2.png')

# driver.close()
