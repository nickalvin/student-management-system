from db import connection
from datetime import date


def create_student():
    reg_number = input("Registration number: ").strip()
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    email = input("Email: ").strip()

    birth_year = int(input("Birth year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    birth_date = date(birth_year, month, day)

    discipline_mark = int(input("Discipline mark: "))
    pocket_money = float(input("Pocket money: "))
    bio = input("Biography: ")

    query = """
        INSERT INTO student
        (reg_number, first_name, last_name, email, birth_date,
         discipline_mark, pocket_money, bio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor = connection.cursor()
    cursor.execute(query, (
        reg_number, first_name, last_name, email, birth_date,
        discipline_mark, pocket_money, bio
    ))
    connection.commit()
    cursor.close()

    print("Student added successfully!")


def get_all_students():
    query = "SELECT * FROM student"

    cursor = connection.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()

    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")


def get_student_by_id():
    student_id = int(input("Enter student ID: "))

    query = "SELECT * FROM student WHERE id = %s"

    cursor = connection.cursor()
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    cursor.close()

    if student:
        print(student)
    else:
        print("Student not found.")


def search_student():
    reg_number = input("Enter registration number: ").strip()

    query = "SELECT * FROM student WHERE reg_number = %s"

    cursor = connection.cursor()
    cursor.execute(query, (reg_number,))
    student = cursor.fetchone()
    cursor.close()

    if student:
        print(student)
    else:
        print("Student not found.")


def search_by_name():
    name = input("Enter first or last name: ").strip()

    query = """
        SELECT * FROM student
        WHERE first_name LIKE %s OR last_name LIKE %s
    """

    cursor = connection.cursor()
    cursor.execute(query, ("%" + name + "%", "%" + name + "%"))
    students = cursor.fetchall()
    cursor.close()

    if students:
        for student in students:
            print(student)
    else:
        print("No matching students found.")


def update_student_email():
    student_id = int(input("Enter student ID: "))
    new_email = input("Enter new email: ").strip()

    query = "UPDATE student SET email = %s WHERE id = %s"

    cursor = connection.cursor()
    cursor.execute(query, (new_email, student_id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Email updated successfully!")
    else:
        print("Student not found or email unchanged.")

    cursor.close()


def update_discipline_mark():
    student_id = int(input("Enter student ID: "))
    new_mark = int(input("Enter new discipline mark: "))

    query = """
        UPDATE student
        SET discipline_mark = %s
        WHERE id = %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (new_mark, student_id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Discipline mark updated successfully!")
    else:
        print("Student not found or mark unchanged.")

    cursor.close()


def update_pocket_money():
    student_id = int(input("Enter student ID: "))
    new_amount = float(input("Enter new pocket money: "))

    query = """
        UPDATE student
        SET pocket_money = %s
        WHERE id = %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (new_amount, student_id))
    connection.commit()

    if cursor.rowcount > 0:
        print("Pocket money updated successfully!")
    else:
        print("Student not found or amount unchanged.")

    cursor.close()


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM student WHERE id = %s",
        (student_id,)
    )
    student = cursor.fetchone()

    if student:
        print("Student details:", student)
        confirmation = input(
            "Are you sure you want to delete this student? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            query = "DELETE FROM student WHERE id = %s"
            cursor.execute(query, (student_id,))
            connection.commit()
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found.")

    cursor.close()


def get_students_by_discipline():
    mark = int(input("Enter minimum discipline mark: "))

    query = """
        SELECT * FROM student
        WHERE discipline_mark < %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (mark,))
    students = cursor.fetchall()
    cursor.close()

    if students:
        for student in students:
            print(student)
    else:
        print("No students found below that mark.")


def get_students_by_birth_year():
    year = int(input("Enter birth year: "))

    query = """
        SELECT * FROM student
        WHERE YEAR(birth_date) = %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (year,))
    students = cursor.fetchall()
    cursor.close()

    if students:
        for student in students:
            print(student)
    else:
        print("No students found for that birth year.")

def count_students():
    query = "SELECT COUNT(*) FROM student"

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    print("Total students:", result[0])

def get_average_discipline():
    query = "SELECT AVG(discipline_mark) FROM student"

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result[0] is not None:
        print("Average discipline mark:", round(result[0], 2))
    else:
        print("There are no student marks to calculate.")


def get_highest_discipline():
    query = """
        SELECT * FROM student
        WHERE discipline_mark = (
            SELECT MAX(discipline_mark) FROM student
        )
    """

    cursor = connection.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()

    if students:
        print("Student(s) with the highest discipline mark:")
        for student in students:
            print(student)
    else:
        print("No students found.")
