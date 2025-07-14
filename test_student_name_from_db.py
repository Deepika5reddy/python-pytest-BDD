import mysql.connector
from decimal import Decimal
import datetime

def test_student_name_from_db():
    try:
        # Step 1: Connect to DB
        connect = mysql.connector.connect(
            host='localhost',
            database='student_grades_db',
            user='root',
            password='$ervices1'
        )

        assert connect.is_connected(), " Not connected to the database"
        cursor = connect.cursor()

        # Step 2: Run query
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()

        # Step 3: Validate first student
        first_row = results[0]
        student_id, name, grade, gpa, enrolled, dob, email = first_row

        assert name == 'Abby Johnson'
        assert grade == 10
        assert gpa == Decimal('3.1')
        assert enrolled == 'Yes'
        assert dob == datetime.date(2008, 5, 14)
        assert email == 'abby.johnson@mavenhighschool.com'

    finally:
        # Step 4: Cleanup
        if 'cursor' in locals():
            cursor.close()
        if 'connect' in locals() and connect.is_connected():
            connect.close()
