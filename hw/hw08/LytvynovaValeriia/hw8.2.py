import cal_area

choice = input("Choose a shape: \n1 - rectangle;\n2 - triangle;\n3 - circle;\n ")

if choice == '1':
    print(cal_area.rectangle_area())
elif choice == '2':
    print(cal_area.triangle_area())
elif choice == '3':
    print(cal_area.circle_area())
else:
    print("Wrong input")

