import mysql.connector

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = '',
	database = 'list_of_Book')

if db.is_connected():
	print("berhasil terhubung")

cursor = db.cursor()
#aktifkan jika hendak membuat database dan matikan ketika hendak membuat tabel
# cursor.execute("CREATE DATABASE list_of_Book") 

print("Database berhasil dibuat")

sql = """CREATE TABLE KumpulanBuku (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Title VARCHAR(255),
  Author VARCHAR(255),
  Date_published DATE,
  Number_of_Pages INT(11),
  Type_of_Book VARCHAR(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")
