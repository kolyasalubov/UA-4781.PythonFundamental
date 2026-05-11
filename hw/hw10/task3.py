class Employee:
    """Клас для представлення співробітника компанії."""
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Загальна кількість співробітників: {cls.employee_count}")

emp1 = Employee("Олена", 2500)
emp2 = Employee("Ігор", 3000)

emp1.display_employee_info()
emp2.display_employee_info()
Employee.display_total_employees()

print("\n--- Інформація про клас ---")
print(f"Базові класи (__base__): {Employee.__base__}")
print(f"Простір імен (__dict__): {Employee.__dict__}")
print(f"Назва класу (__name__): {Employee.__name__}")
print(f"Назва модуля (__module__): {Employee.__module__}")
print(f"Документація (__doc__): {Employee.__doc__}")