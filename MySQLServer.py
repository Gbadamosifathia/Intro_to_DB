import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="best1est6..."
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS topzee_book_store")
    print("Database 'topzee_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    mycursor.close()
    mydb.close()
