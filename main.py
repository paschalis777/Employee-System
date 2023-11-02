import pandas as pd
import psycopg2
from classEmployee import Employee

conn = None


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
    conn = psycopg2.connect(database="",
                            user="",
                            password="",
                            host="", port="")



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




