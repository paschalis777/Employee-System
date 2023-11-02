# Employee-System
The provided Python application performs the following tasks:

1. **Data Import and Preprocessing**: It loads data from a CSV file, `employeedata.csv`,
2. using the Pandas library. The CSV file contains employee information, including their first name, last name, age, city, salary, and department.
3. The application performs data preprocessing by filling missing values in the "age" and "salary"
4. columns with their respective means and converting these columns to integers.

5. **Object Creation**: The application creates a list of `Employee` objects, where each object represents an employee with attributes such as
6. first name, last name, age, city, salary, and department. These objects are created based on the data imported from the CSV file.

7. **Data Analysis and Filtering**: It provides summary statistics for the "age" and "salary" columns using `describe()`. Additionally,
8. it filters and prints the names and ages of employees over 30 years old.

9. **Employee Bonus**: It demonstrates giving a bonus to an employee. An employee named "John Doe" receives a 10% salary bonus, and the new salary is displayed.

10. **Changing Department**: Another employee, "Jane Smith," changes her department to "PHIZER," and the updated department is displayed.

11. **Database Connection**: The application establishes a connection to a PostgreSQL database using the provided credentials
12. (database name, username, password, host, and port).

13. **Database Table Creation**: It creates a table named "EMPLOYEE_TABLE" in the PostgreSQL database to store employee information.

14. **Data Insertion**: It attempts to insert employee data into the database table. However, this part of the code is currently commented out.

15. **Data Retrieval**: It retrieves data from the "EMPLOYEE_TABLE" and prints the results.

In summary, the application loads and preprocesses employee data from a CSV file, creates `Employee` objects, performs data analysis, 
allows for bonus and department changes, and connects to a PostgreSQL database to store and retrieve employee information. Please note 
that the code for inserting data into the database is currently commented out, but it can be enabled to store employee data in the database.
