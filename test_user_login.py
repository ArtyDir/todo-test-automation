import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_login_button_in_body_exists():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://django-todo.org/')

    # переход к начальной странице из тела сайта
    body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
    body_elem.click()

    driver.close()


def test_login_button_in_header_exists():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://django-todo.org/')

    # переход к начальной странице из шапки сайта
    head_elem = driver.find_element(By.XPATH, '//nav//a[@href="/login"]')
    head_elem.click()

    driver.close()


@pytest.mark.parametrize('username, password', [
    ('user1', 'todo'),
    ('user2', 'todo'),
    ('user3', 'todo'),
    ('user4', 'todo'),
    ('staffer', 'todo')
])
def test_user_login(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://django-todo.org/')

    # переход к странице логина
    body_elem = driver.find_element(By.XPATH, '//main//a[@href="/login"]')
    body_elem.click()

    # ввод имени пользователя
    username_elem = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_elem.send_keys(username)

    # ввод пароля пользователя
    password_elem = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_elem.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    login_button.click()

    # разлогинивание пользователя
    logout = driver.find_element(By.XPATH, '//a[@href="/logout"]')
    logout.click()

    driver.close()
