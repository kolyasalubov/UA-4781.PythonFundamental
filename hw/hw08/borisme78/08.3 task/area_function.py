import math


def get_float(a: str) -> float:
    """
    Зчитує від користувача числове значення з клавіатури.

    Повторює запит доки користувач не введе коректне число.

    Args:
        prompt: Підказка яка відображається користувачу.

    Returns:
        Числове значення введене користувачем.

    Example:
        >>> get_float("Введіть ширину: ")
        Введіть ширину: abc
        Помилка. Введіть числове значення
        Введіть ширину: 5.3
        5.3
    """
    while True:
        try:
            return float(input(a))
        except ValueError:
            print('Помилка. Введіть чиcлове значення')





def area_rectangle(width: float, length: float) -> float:
    '''
    Функція що обчислює площу прямокутника.
    Вхідні значення width : float, length : float, 
    Формула width * length
    Повертає площу :float
    '''
    return width * length




def area_triangle(base : float, height : float) -> float:
    '''
    Функція що обчислює площу трикутника.
    Вхідні значення base : float, height : float, 
    Формула 0.5 * base * height
    Повертає площу :float
    '''
    return 0.5 * base * height





def area_circle(radius: float):
    '''
    Функція що обчислює площу трикутника.
    Вхідні значення radius : float,
    Формула pi * radius**2
    Повертає площу :float
    '''
    return math.pi * radius**2
