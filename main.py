import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from test_create_task import test_create_task
from test_user_login import test_login_button_in_body_exists, test_login_button_in_header_exists, test_user_login


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

    button_done_in_body = driver.find_element(By.XPATH, '//main//button[@name="toggle_done"]')
    button_done_in_body.click()
    time.sleep(2)

    driver.save_screenshot(screenshot)

    driver.close()


def main():
    test_login_button_in_body_exists()
    test_login_button_in_header_exists()
    test_user_login('user1', 'todo')
    test_user_login('user2', 'todo')
    test_user_login('user3', 'todo')
    test_user_login('user4', 'todo')
    test_user_login('staffer', 'todo')
    test_create_task('user1', 'todo', 'New task1_1', 'Tanya Stewart (user1)', 'screen_user1_1.png')
    test_create_task('user1', 'todo', 'New task1_2', 'Brittany Wright (user2)', 'screen_user1_2.png')
    test_create_task('user2', 'todo', 'New task2_1', 'Tanya Stewart (user1)', 'screen_user2_1.png')
    test_create_task('user2', 'todo', 'New task2_2', 'Brittany Wright (user2)', 'screen_user2_2.png')
    test_create_task('user1', 'todo', 'New task1_s', 'Matthew Gonzalez (staffer)', 'screen_user1_s.png')
    test_create_task('user2', 'todo', 'New task2_s', 'Matthew Gonzalez (staffer)', 'screen_user2_s.png')
    test_create_task('user3', 'todo', 'New task3_3', 'Brian Harris (user3)', 'screen_user3_3.png')
    test_create_task('user3', 'todo', 'New task3_4', 'Linda Tucker (user4)', 'screen_user3_4.png')
    test_create_task('user4', 'todo', 'New task4_3', 'Brian Harris (user3)', 'screen_user4_3.png')
    test_create_task('user4', 'todo', 'New task4_4', 'Linda Tucker (user4)', 'screen_user4_4.png')
    test_create_task('user3', 'todo', 'New task3_s', 'Matthew Gonzalez (staffer)', 'screen_user3_s.png')
    test_create_task('user4', 'todo', 'New task4_s', 'Matthew Gonzalez (staffer)', 'screen_user4_s.png')
    test_create_task('staffer', 'todo', 'New tasks_s', 'Adrienne Welch (staffer)', 'screen_users_s.png')
    test_create_task('staffer', 'todo', 'New tasks_3', 'Brian Harris (user3)', 'screen_users_3.png')
    test_create_task('staffer', 'todo', 'New tasks_4', 'Linda Tucker (user4)', 'screen_users_4.png')
    test_create_list('staffer', 'todo', 'Added list Scuba', 'Scuba Divers', 'screen_scuba.png')
    test_create_list('staffer', 'todo', 'Added list Basket', 'Basket Weavers', 'screen_basket.png')
    test_task_done('staffer', 'todo', 'screen_done.png')
    test_task_mark_done('staffer', 'todo', 'screen_mark_done.png')


if __name__ == '__main__':
    main()

# driver.close()
