import math

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return (h / 2) * a

def circle_area(r):
    return math.pi * r**2

print('Available figures: rectangle, triangle, circle')
figure = input('What figure area you want? ')

if figure == 'rectangle':
    a = float(input('input a:'))
    b = float(input('input b:'))
    print(rectangle_area(a, b))

elif figure == 'triangle':
    a = float(input('input a:'))     
    h = float(input('input h:'))
    print(triangle_area(a, h))

elif figure == 'circle': 
    r = float(input('input radius:'))
    print(circle_area(r))

else:
    print('Invalid figure.') 

