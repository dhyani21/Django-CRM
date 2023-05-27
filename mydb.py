import mysql.connector as con

dataBase = con.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE databased")

print('Success!')
