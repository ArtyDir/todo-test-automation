import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv


@pytest.mark.parametrize('username, password, screenshot', [
    ('staffer', 'todo', 'screen_django_todo.png'),
])
def test_header_django_todo(username, password, screenshot):
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

    django_todo = driver.find_element(By.XPATH, '//a[@class="navbar-brand"]')
    django_todo.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [
    ('staffer', 'todo', 'screen_todo_list.png'),
])
def test_header_todo_lists(username, password, screenshot):
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

    todo_lists = driver.find_element(By.XPATH, '//header//li[1]/a')
    todo_lists.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [
    ('staffer', 'todo', 'screen_my_task.png'),
])
def test_header_my_tasks(username, password, screenshot):
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

    my_tasks = driver.find_element(By.XPATH, '//li[2]/a')
    my_tasks.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [
    ('staffer', 'todo', 'screen_log_out.png'),
])
def test_header_log_out(username, password, screenshot):
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

    log_out = driver.find_element(By.XPATH, '//li[3]/a')
    log_out.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [
    ('staffer', 'todo', 'screen_file_ticket.png'),
])
def test_header_file_ticket(username, password, screenshot):
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

    file_ticket = driver.find_element(By.XPATH, '//li[4]/a')
    file_ticket.click()

    title = driver.find_element(By.XPATH, '//input[@name="title"]')
    title.send_keys('Test')

    description = driver.find_element(By.XPATH, '//textarea[@id="id_note"]')
    description.send_keys('Test-Test-Test')

    submit = driver.find_element(By.XPATH, '//input[@name="add_task"]')
    submit.click()

    driver.save_screenshot(screenshot)

    driver.close()


@pytest.mark.parametrize('username, password, screenshot', [
    ('staffer', 'todo', 'screen_import.png'),
])
def test_import(username, password, screenshot):
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

    task_list = driver.find_element(By.XPATH, '//main/ul[2]/li[1]/a')
    task_list_text = task_list.text

    file_path = '/Users/artem/Documents/Postman:files/test_csv.csv'

    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ['Title', 'Group', 'Task List', 'Created By', 'Created Date', 'Due Date', 'Completed', 'Assigned To',
             'Note', 'Priority'])
        csv_writer.writerow(['Make dinner', 'Basket Weavers', task_list_text, username, '', '2019-06-14', 'No', 'user1',
                             'This is note one', 3])

    import_button = driver.find_element(By.XPATH, '//li[5]/a')
    import_button.click()

    file_input = driver.find_element(By.XPATH, '//input[@name="csvfile"]')
    file_input.send_keys(file_path)

    upload = driver.find_element(By.XPATH, '//button[text()="Upload"]')
    upload.click()

    # Title,Group,Task List,Created By,Created Date,Due Date,Completed,Assigned To,Note,Priority
    # Make dinner,Basket Weavers,Zip,user1,,2019-06-14,No,user1,This is note one,3
    # Bake bread,Basket Weavers,Zip,user1,2012-03-14,,Yes,,,
    # Bring dessert,Basket Weavers,Zap,user2,2015-06-24,,,,This is note two,77

    driver.save_screenshot(screenshot)

    driver.close()
