import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.parametrize('username, password, title, group, screenshot', [
    ('staffer', 'todo', 'Added list Scuba', 'Scuba Divers', 'screen_scuba.png'),
    ('staffer', 'todo', 'Added list Basket', 'Basket Weavers', 'screen_basket.png'),
])
def test_create_list(username, password, title, group, screenshot):
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

    # создание нового списка
    list = driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
    list.click()

    list_title = driver.find_element(By.XPATH, '//input[@id="id_name"]')
    list_title.send_keys(title)

    group_to = driver.find_element(By.XPATH, f'//select[@id="id_group"]/option[text()="{group}"]')
    group_to.click()

    submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, title, group, screenshot', [
    ('staffer', 'todo', 'Added Test list', 'Scuba Divers', 'screen_delete.png'),
])
def test_delete_list(username, password, title, group, screenshot):
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

    # создание нового списка
    list = driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
    list.click()

    list_title = driver.find_element(By.XPATH, '//input[@id="id_name"]')
    list_title.send_keys(title)

    group_to = driver.find_element(By.XPATH, f'//select[@id="id_group"]/option[text()="{group}"]')
    group_to.click()

    submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    button_lists = driver.find_element(By.XPATH, '//div/ul/li[1]/a')
    button_lists.click()

    # удаление списка
    list_to_delete = driver.find_element(By.XPATH, f'//a[text()="{title}"]')
    list_to_delete.click()

    delete_button = driver.find_element(By.XPATH, '//a[text()="Delete this list"]')
    delete_button.click()

    button_do_it = driver.find_element(By.XPATH, '//input[@name="delete-confirm"]')
    button_do_it.click()

    driver.save_screenshot(screenshot)

    driver.close()
