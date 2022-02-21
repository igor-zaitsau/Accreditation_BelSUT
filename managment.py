import time
import sqlite3
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


LOGIN = input('ENTER YOUR LOGIN: ')
PASSWORD = input('ENTER YOUR PASSWORD: ')


def function():
    time.sleep(1)
    question = driver.find_element(By.CLASS_NAME, 'qtext').text

    temp = 1

    for em in cursor.execute("SELECT question FROM Managment"):
        if question == em[0]:
            #print("Вопрос уже есть в БД")
            time.sleep(1)
            temp = 0
            cursor.execute(f"SELECT answer FROM Managment WHERE question = (?) LIMIT 1", [question])
            result = cursor.fetchone()
            if result[0] == None:
                #print("Ответа нет в БД!")
                time.sleep(1)
                random_answer(question)
            elif result[0] != None:
                #print("Ответ есть в БД!")
                #time.sleep(2)

                answer1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/label').text
                answer2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/label').text
                answer3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/label').text
                answer4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[4]/label').text

                try:
                    answer5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[5]/label').text
                except NoSuchElementException:
                    answer5 = 0
                if result[0] == answer1[3:]:
                    time.sleep(7)
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/input').click()
                    time.sleep(8)
                    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()
                    time.sleep(1)
                elif result[0] == answer2[3:]:
                    time.sleep(7)
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/input').click()
                    time.sleep(8)
                    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()
                    time.sleep(1)
                elif result[0] == answer3[3:]:
                    time.sleep(7)
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/input').click()
                    time.sleep(8)
                    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()
                    time.sleep(1)
                elif result[0] == answer4[3:]:
                    time.sleep(7)
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[4]/input').click()
                    time.sleep(8)
                    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()
                    time.sleep(1)
                elif result[0] == answer5[3:] and answer5 != 0:
                    time.sleep(7)
                    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[5]/input').click()
                    time.sleep(8)
                    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()
                    time.sleep(1)


    if temp == 1:
        cursor.execute("INSERT INTO Managment (question) VALUES (?)", [question])
        sqlite_connection.commit()
        #print("Вопрос добавлен в БД!")
        time.sleep(1)
        random_answer(question)


def random_answer(question):
    q = random.randint(1, 5)

    if q == 1:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()

        try:
            answer = driver.find_element(By.CLASS_NAME, 'rightanswer').text
            answer = answer[18:]
            cursor.execute("UPDATE Managment SET answer = (?) WHERE question = (?)", [answer, question])
            sqlite_connection.commit()
            #print("Ответ верный и он добавлен в БД!!! = " + answer)
            time.sleep(1)
        except NoSuchElementException:
            #print("Ответ неверный")
            time.sleep(1)

    elif q == 2:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()

        try:
            answer = driver.find_element(By.CLASS_NAME, 'rightanswer').text
            answer = answer[18:]
            cursor.execute("UPDATE Managment SET answer = (?) WHERE question = (?)", [answer, question])
            sqlite_connection.commit()
            #print("Ответ верный и он добавлен в БД!!! = " + answer)
            time.sleep(1)
        except NoSuchElementException:
            #print("Ответ неверный")
            time.sleep(1)

    elif q == 3:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()

        try:
            answer = driver.find_element(By.CLASS_NAME, 'rightanswer').text
            answer = answer[18:]
            cursor.execute("UPDATE Managment SET answer = (?) WHERE question = (?)", [answer, question])
            sqlite_connection.commit()
            #print("Ответ верный и он добавлен в БД!!! = " + answer)
            time.sleep(1)
        except NoSuchElementException:
            #print("Ответ неверный")
            time.sleep(1)

    elif q == 4:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[4]/input').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()

        try:
            answer = driver.find_element(By.CLASS_NAME, 'rightanswer').text
            answer = answer[18:]
            cursor.execute("UPDATE Managment SET answer = (?) WHERE question = (?)", [answer, question])
            sqlite_connection.commit()
            #print("Ответ верный и он добавлен в БД!!! = " + answer)
            time.sleep(1)
        except NoSuchElementException:
            #print("Ответ неверный")
            time.sleep(1)

    elif q == 5:
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[2]/div[2]/div[5]/input').click()
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[1]/div[2]/div/div[3]/input').click()
        except NoSuchElementException:
            random_answer(question)

        try:
            answer = driver.find_element(By.CLASS_NAME, 'rightanswer').text
            answer = answer[18:]
            cursor.execute("UPDATE Managment SET answer = (?) WHERE question = (?)", [answer, question])
            sqlite_connection.commit()
            #print("Ответ верный и он добавлен в БД!!! = " + answer)
            time.sleep(1)
        except NoSuchElementException:
            #print("Ответ неверный")
            time.sleep(1)


driver = webdriver.Firefox()
driver.get('http://dist.bsut.by/login/index.php')

driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(LOGIN)

driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys(PASSWORD)

driver.find_element(By.ID, "loginbtn").click()

driver.get('http://dist.bsut.by/mod/quiz/view.php?id=7507')

try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section/div/div[1]/div[3]/div/form').click()
except:
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section/div/div[1]/div[2]/div/form').click()



try:
    sqlite_connection = sqlite3.connect('accreditation.db')
    cursor = sqlite_connection.cursor()


    x = 0
    while x < 50:
        function()
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[2]/input[2]').click()
        except:
            driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/form/div/div[2]/input').click()
        x += 1

    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[1]/div/div[1]/div[3]/div/div/form').click()
    #time.sleep(1)
    #driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section[2]/aside/aside/div/div/div[2]/a[2]').click()
    #time.sleep(1)
    cursor.close()
    #driver.quit()

except sqlite3.Error as error:
    print("Ошибка при подключении к БД - ", error)
