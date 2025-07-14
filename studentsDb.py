import mysql.connector
# host, database , user, password
connect=mysql.connector.connect(host = 'localhost', database = 'student_grades_db', user = 'root',password ='$ervices1')
print(connect.is_connected())
cursor = connect.cursor()
cursor.execute("Select * from students")
results = cursor.fetchall()
print(results)
first_row = results[0]
print(first_row)
student_name  = first_row[1]
print(student_name)
assert student_name == 'Abby Johnson'