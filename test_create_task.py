import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.parametrize('username, password, assigned', [
    ('user1', 'todo', 'user1'),
    ('user1', 'todo', 'user2'),
    ('user2', 'todo', 'user1'),
    ('user2', 'todo', 'user2'),
    ('user1', 'todo', 'staffer'),
    ('user2', 'todo', 'staffer'),
    ('user3', 'todo', 'user3'),
    ('user3', 'todo', 'user4'),
    ('user4', 'todo', 'user3'),
    ('user4', 'todo', 'user4'),
    ('user3', 'todo', 'staffer'),
    ('user4', 'todo', 'staffer'),
    ('staffer', 'todo', 'staffer'),
    ('staffer', 'todo', 'user3'),
    ('staffer', 'todo', 'user4')
])
def test_create_task(username, password, assigned):
    title = f'New task {username} for {assigned}'
    screenshot = f'screen_{username}_{assigned}.png'

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
    # добавление ожидания для исключения ошибок тестов
    task_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@id="id_title"]')))
    task_title.send_keys(title)

    description = driver.find_element(By.XPATH, '//textarea[@id="id_note"]')
    description.send_keys('La-la-la')

    date = driver.find_element(By.XPATH, '//input[@type="date"]')
    date.send_keys('30.03.2023')

    assigned_to = driver.find_element(By.XPATH,
                                      f'//select[@name="assigned_to"]/option[contains(text(), " ({assigned})")]')
    assigned_to.click()

    submit = driver.find_element(By.XPATH, '//input[@name="add_edit_task"]')
    submit.click()
    driver.save_screenshot(screenshot)

    driver.close()
