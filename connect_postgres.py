import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_user",
                        password="db_pass",
                        port="db_port")

cursor = conn.cursor()
cursor.execute("SELECT * FROM example_table")
print(cursor.fetchone())
print(cursor.fetchall())
print(cursor.fetchmany(size=5))

conn.close()


import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
Connection established to: (
   'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
)
