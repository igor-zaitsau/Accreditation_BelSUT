import sqlite3

sqlite_connection = sqlite3.connect('accreditation.db')
cursor = sqlite_connection.cursor()

f = open('managment.txt', 'w')
x = 1

for em in cursor.execute("SELECT * FROM Managment"):
    f.write(str(x) + '. ' + str(em[0]) + ' | ' + str(em[1]) + '\n')
    x = x + 1