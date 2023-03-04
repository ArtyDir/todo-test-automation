from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_create_task(username, password, title, assigned, screenshot):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://django-todo.org/')

    # ввод имени пользователя
    body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
    body_elem.click()

    username_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_elem.send_keys(username)

    # ввод пароля пользователя
    password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_elem.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    login_button.click()

    # создание задачи пользователя
    list = driver.find_element(By.XPATH, '//main/ul[1]/li[1]/a')
    list.click()

    task = driver.find_element(By.XPATH, '//button[@id="AddTaskButton"]')
    task.click()

    task_title = driver.find_element(By.XPATH, '//input[@id="id_title"]')
    task_title.send_keys(title)

    description = driver.find_element(By.XPATH, '//textarea[@id="id_note"]')
    description.send_keys('La-la-la')

    date = driver.find_element(By.XPATH, '//input[@type="date"]')
    date.send_keys('30.03.2023')

    assigned_to = driver.find_element(By.XPATH, f'//select[@name="assigned_to"]/option[text()="{assigned}"]')
    assigned_to.click()

    submit = driver.find_element(By.XPATH, '//input[@name="add_edit_task"]')
    submit.click()
    driver.save_screenshot(screenshot)

    driver.close()
