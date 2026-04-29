#Task 1. Напиши функцию которая возвращает наибольшее из двух чисел. Использовать докстрингу.


def number_list(num1,num2):

    '''
      This function print biggest number between 2 selection
      input parametrs : num but it's int.
      output : nummber
      '''


    if num1 > num2:
        print(f"num1 {num1} it's biggest then {num2}")
        return num1
    else :
        print(f"num1 : {num1} it's less then {num2}")
        return num2