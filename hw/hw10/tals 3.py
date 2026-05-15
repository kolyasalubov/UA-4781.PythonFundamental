class Employee():

    count=0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
        Employee.count+=1

    def sum_employeers(self):
        print(Employee.count)

    def information_method(self):
        return (f"{self.name} and {self.salary}")
    

emp1 = Employee("Jimmy",25.000)

emp1.sum_employeers()

print(emp1.information_method())

emp2=Employee("Michu",35.000)

emp2.sum_employeers()

print(emp2.information_method())


print(Employee.__name__)

print(Employee.__dict__)

print(Employee.__base__)

print(Employee.__module__)

print(Employee.__doc__)

##############################################


