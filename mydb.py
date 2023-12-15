import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)

# preparar un objeto de cursor
cursorObject = dataBase.cursor()

# crear una base de datos
cursorObject.execute("CREATE DATABASE test")

print("Se hizo bien :D ")
