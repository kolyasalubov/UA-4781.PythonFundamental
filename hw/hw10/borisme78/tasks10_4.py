##############################################

class Ball:
    def __init__(self, ball_type = 'regular'):
        self.ball_type = ball_type
    

ball1 = Ball()
ball2 = Ball('Super')
print(ball1.ball_type)
print(ball2.ball_type)

##############################################

import random 
class Ghost:

    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)

ghost = Ghost()

print(ghost.color)

##############################################

class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        pass

class Woman(Human):
    def __init__(self):
        pass        

def God():
    adam = Man()
    eve = Woman()
    return[adam, eve]

#############################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        
        return f"{self.name}s age is {self.age}"

per1 = Person("John", 34)
print(per1.info)

#############################################

import math

class Sphere:
    def __init__(self,radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        result = (4/3) * math.pi * (self.radius ** 3)
        return round(result, 5)

    def get_surface_area(self):
        result = 4 * math.pi * (self.radius ** 2)
        return round(result, 5)

    def get_density(self):
        result = self.mass / self.get_volume()
        return round(result, 5)
    
ball = Sphere(2, 50)

print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())

#############################################

def class_name_changer(cls, new_name):
    if not (new_name[0].isupper() and new_name.isalnum()):
        raise ValueError('Invalid class name')
    cls.__name__ = new_name
    return cls


class MyClass:
    pass

class_name_changer(MyClass, 'NewClass')
print(MyClass.__name__)
