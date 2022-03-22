import time
import sqlite3
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


LOGIN = 'zajcev9e9'
PASSWORD = 'myblfvrpug'


def function():
    time.sleep(1)
    question = driver.find_element(By.CLASS_NAME, 'qtext').text
    time.sleep(2)
    answer = driver.find_element(By.CLASS_NAME, 'rightanswer').text
    answer = answer[18:]

    cursor.execute("INSERT INTO OOP (question) VALUES (?)", [question])
    sqlite_connection.commit()
    cursor.execute("UPDATE OOP SET answer = (?) WHERE question = (?)", [answer, question])
    sqlite_connection.commit()





driver = webdriver.Firefox()
driver.get('http://dist.bsut.by/login/index.php')

driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(LOGIN)

driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys(PASSWORD)

driver.find_element(By.ID, "loginbtn").click()

driver.get('http://dist.bsut.by/mod/quiz/review.php?attempt=31160#')



try:
    sqlite_connection = sqlite3.connect('accreditation.db')
    cursor = sqlite_connection.cursor()


    x = 0
    while x < 400:
        function()
        try:
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/div/a[2]').click()
        except:
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/div/a').click()
        x += 1

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к БД - ", error)
