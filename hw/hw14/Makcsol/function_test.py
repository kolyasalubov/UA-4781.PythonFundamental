import unittest

import functions


class MyClass(unittest.TestCase):
    def test_func(self):
        self.assertEqual(functions.greeting_by_name("Maksym"),"Hello Maksym!","is Failed")
    def test_symbol(self):
        self.assertEqual(functions.get_symbol_position("World","o"),2)
    def test_symbols(self):
        self.assertEqual(functions.get_symbol_position("Python","d"),"Not found")
    def test_symbols_reserv(self):
        self.assertEqual(functions.get_symbol_position("Hello","ab"),"Error! Symbol can be string with only one letter")
    def test_last_dict(self):
        self.assertEqual(functions.merge({"a":1},{"b":2}),{"a":1,"b":2},"Dicts not connect")
    
if __name__ == '__main__':
    unittest.main()


import functions_with_errors

class Mytestclass(unittest.TestCase):
    def test_dict_equal(self):
        self.assertEqual(functions_with_errors.greeting_by_name("Dmitry"),"Hello Dmitry!")
    def test_find_symbol(self):
        self.assertEqual(functions_with_errors.get_symbol_position("Web-developer","e"),"Web-developer")
    def test_list_symbol(self):
        d1={"a":1}
        self.assertEqual(functions_with_errors.merge(d1,{"b":2}),{"a":1},"Dicts not connect")


if __name__ == '__main__':
    unittest.main() 