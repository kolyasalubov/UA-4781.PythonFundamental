'''
Task1

'''
class Polygon:
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length


class Rectangle(Polygon):

    def area_rectangle(self) -> float:

        return self.width * self.length
    

rect = Rectangle(3,3)
print(rect.area_rectangle())

###########################################################
'''
Task2.
'''
class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
     print(f'Hello {self.name}')

    @classmethod
    def homo(cls):
        return "Це представник роду 'Homosapiens' "
    
    @staticmethod
    def information():
        return "Homo sapiens -  означає 'людина розумна'"
    
a = Human('Igor')

a.hello()

print(Human.homo())
print(Human.information())

################################################

'''
Task3.
'''
class Employee:
    '''
    Цей клас описує співробітників компанії та рахує їх загальну кількість.
    '''
    count_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count_employee += 1

    
    @classmethod
    def employee_count(cls):
        return f'Загальна кількість співробітників: {Employee.count_employee}'



    def information_eployee(self):

        return f'Моє імя {self.name}, і я отримую {self.salary} зарплати.' 


emp1 = Employee('Igor', 2000)
emp2 = Employee('Stepan', 2500)
emp3 = Employee('Anna', 3000)

print(emp1.information_eployee())
print(emp2.information_eployee())
print(emp3.information_eployee())
print(Employee.employee_count())

print(f"\nІнформація про клас:")
print(f"Базові класи (__bases__): {Employee.__bases__}")
print(f"Простір імен (__dict__): {Employee.__dict__}")
print(f"Ім'я класу (__name__): {Employee.__name__}")
print(f"Модуль (__module__): {Employee.__module__}")
print(f"Документація (__doc__): {Employee.__doc__}")



