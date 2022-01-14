import mysql.connector
my_connection = mysql.connector.connect(host = "localhost", user = "root",passwd = "rootpassword",database="briandb")
print(my_connection)
my_cursor=my_connection.cursor()
print(my_cursor)
try:
    data_base=my_cursor.execute("show databases")
except:
    my_connection.rollback()
for x in my_cursor:
    print(x)
#my_connection.close()
my_cursor.execute("CREATE DATABASE mysql_conectordb")
my_cursor.execute("SHOW DATABASES")
for x in my_cursor:
    print(x)