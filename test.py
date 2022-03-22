import sqlite3

sqlite_connection = sqlite3.connect('accreditation.db')
cursor = sqlite_connection.cursor()

f = open('oop.txt', 'w')
x = 1

for em in cursor.execute("SELECT * FROM OOP"):
    f.write(str(x) + '. ' + str(em[0]) + ' | ' + str(em[1]) + '\n')
    x = x + 1