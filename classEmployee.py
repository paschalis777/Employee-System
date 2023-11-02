class Employee():
    def __init__(self, first_name, last_name, age, city, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.salary = salary
        self.department = department

    def displayInfo(self):
        return f' Ονομα: {self.first_name} Επίθετο: {self.last_name}, Ηλικία: {self.age} πολη: {self.city} Μισθός: ${self.salary}, Τμήμα: {self.department}'

    def self_bonus(self, bonus_percent):
        self.salary = int(self.salary)
        bonus_amount = self.salary * bonus_percent / 100
        self.salary += bonus_amount

    def change_department(self, new_department):
        self.department = new_department
