def get_max (a, b):
    """ Повертає найбільше з двох чисел.
    Args:
        a: перше число
        b: друге число
    Returns:
        Найбільше з двох чисел (а або б)
    """
    if a > b:
        return a
    return b

print(get_max.__doc__)
