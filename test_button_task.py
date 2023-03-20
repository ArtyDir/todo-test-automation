import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.parametrize('username, password, screenshot', [('staffer', 'todo', 'screen_done.png')])
def test_task_done(username, password, screenshot):
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

    # выбор первого списка задач
    list = driver.find_element(By.XPATH, '//main/ul[1]/li[1]/a')
    list.click()

    button_done = driver.find_element(By.XPATH, '//tr[2]//button')
    button_done.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [('staffer', 'todo', 'screen_mark_done.png')])
def test_task_mark_done(username, password, screenshot):
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

    # выбор первого списка задач
    list = driver.find_element(By.XPATH, '//main/ul[1]/li[1]/a')
    list.click()

    task = driver.find_element(By.XPATH, '//main//tr[2]')
    task.click()

    button_mark_done = driver.find_element(By.XPATH, '//main//button[@name="toggle_done"]')
    button_mark_done.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot, assigned',
                         [('staffer', 'todo', 'screen_edit.png', 'staffer')])
def test_edit_task(username, password, screenshot, assigned):
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

    # выбор первого списка задач
    list = driver.find_element(By.XPATH, '//main/ul[1]/li[1]/a')
    list.click()

    task = driver.find_element(By.XPATH, '//main//tr[2]/td/a')
    task.click()

    # редактирование задачи
    button_edit = driver.find_element(By.XPATH, '//button[@id="EditTaskButton"]')
    button_edit.click()

    # назначение задачи пользователю
    assigned_to = driver.find_element(By.XPATH,
                                      f'//select[@name="assigned_to"]/option[contains(text(), " ({assigned})")]')
    assigned_to_temporary = f'//select[@name="assigned_to"]/option[contains(text(), " ({assigned})")]'
    print(assigned_to_temporary)
    assigned_to.click()

    # подтверждение редактирования
    submit = driver.find_element(By.XPATH, '//input[@name="add_edit_task"]')
    submit.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [('staffer', 'todo', 'screen_delete.png')])
def test_delete_task(username, password, screenshot):
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

    # выбор первого списка задач
    list = driver.find_element(By.XPATH, '//main/ul[1]/li[1]/a')
    list.click()

    task = driver.find_element(By.XPATH, '//main//tr[2]/td/a')
    task.click()

    # удаление задачи
    button_edit = driver.find_element(By.XPATH, '//button[@name="submit_delete"]')
    button_edit.click()

    driver.save_screenshot(screenshot)

    driver.close()
