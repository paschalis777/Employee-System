import pandas as pd
import psycopg2
from classEmployee import Employee

conn = None
# (?????)

try:
    df = pd.read_csv("data/employeedata.csv", delimiter=";")

    # print(df.head())   ΓΙΑ ΝΑ ΠΕΡΝΩ ΜΟΝΟ ΤΑ HEAD
    print(df.to_string())

    df['age'].fillna(df['age'].mean(), inplace=True)
    df['salary'].fillna(df['salary'].mean(), inplace=True)

    df['age'] = df['age'].astype(int)
    df['salary'] = df['salary'].astype(int)


    print("----------------------------------------------------------------------------------------------")

    print(df[["age", "salary"]].describe())

    Employee_list = []
    for index, row in df.iterrows():
        employee = Employee(row["first_name"], row["last_name"], row["age"], row["city"], row["salary"],
                            row["department"])
        Employee_list.append(employee)

    print("--------------------------------------------------------------------------------------------------")

    for employee in Employee_list:
        print(employee.first_name, employee.last_name, employee.age, employee.city, employee.department)

    print("-----------------------------------------------------------------------------------------------------")

    for employee in Employee_list:
        if employee.age > 30:
            print(employee.first_name, employee.age)

    print("------------------------------------------------------------------------------------------------------")

    employee = Employee("John", "Doe", 35, "new york", "70000", "Marketing")
    employee.self_bonus(10)
    print("NEW SALARY WITH BONYS :", employee.salary)

    print("-------------------------------------------------------------------------------------------------------")

    employee = Employee("Jane", "Smith", 45, "Francisco", 85000, "Engineering")
    employee.change_department("PHIZER")
    print("YOUR NEW DEPARTMENT IS :", employee.department)

    print("-------------------------------------------------------------------------------------------------------")

except Exception as e:
    print(e)

try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="2171985",
                            host="localhost", port="5432")



    if conn:
        print("Σύνδεση στη βάση δεδομένων πραγματοποιήθηκε επιτυχώς.")


    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE_TABLE ( id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name "
                "VARCHAR(255),"
                "age INTEGER, city VARCHAR(255), salary INTEGER, department VARCHAR(255) ); ")

    conn.commit()

    # for employee in Employee_list:
    #     cur.execute("INSERT INTO EMPLOYEE_TABLE (first_name ,last_name,age,city,salary,department) VALUES (%s,%s,%s,"
    #                 "%s,%s,%s)",
    #                 (employee.first_name, employee.last_name, employee.age, employee.city, employee.salary,
    # #                  employee.department))
    #     conn.commit()

    cur.execute("SELECT * FROM EMPLOYEE_TABLE")
    rows = cur.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print(e)

finally:
    if conn:
        conn.close()





    # ??????????????????????
    # 123.2422.23.142
    # username
    # dsnjdk73bjdn
    # booking - backoffice
    # 6541


# Σύνδεση στη βάση δεδομένων πραγματοποιήθηκε επιτυχώς.
# (1, 'John', 'Doe', 35, 'New York', 70000, 'Marketing')
# (2, 'Jane', 'Smith', 45, 'Francisco', 85000, 'Engineering')
# (3, 'Michael', 'Johnson', 32, 'Los Angeles', 60000, 'HR')
# (4, 'Emily', 'Garcia', 18, 'Chicago', 90000, 'Engineering')
# (5, 'William', 'Martinez', 28, 'Houston', 72000, 'Marketing')
# (6, 'Laura', 'Rodriguez', 64, 'Miami', 61000, 'HR')
# (7, 'James', 'Wilson', 61, 'Seattle', 88000, 'Engineering')
# (8, 'Olivia', 'Brow', 25, 'Diego', 71000, 'Marketing')
# (9, 'Liam', 'Miller', 55, 'Dallas', 86000, 'Engineering')
# (10, 'Sophia', 'Anderson', 47, 'Boston', 59000, 'HR')
# (11, 'David', 'Wilson', 52, 'Austin', 72000, 'Marketing')
# (12, 'Emma', 'Brow', 22, 'Detroit', 87000, 'Engineering')
# (13, 'Ethan', 'Miller', 31, 'Phoenix', 71000, 'Marketing')
# (14, 'Olivia', 'Brow', 67, 'Denver', 89000, 'Engineering')
# (15, 'Aiden', 'Martinez', 21, 'Atlanta', 60000, 'HR')
