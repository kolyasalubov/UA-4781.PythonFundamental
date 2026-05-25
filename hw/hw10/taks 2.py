class Human():
    def __init__(self,name):
        self.name = name
        
    def classic_method(self):
        print(f"Hello, my dear {self.name}!I'm glade to see you")

    @classmethod

    def class_method(cls):
        return "This kind of Homosapiens"
    

    @staticmethod

    def static_method():
        return "Something message"
    

a1 = Human("Alex")

a1.classic_method()

#Hello, my dear Alex!I'm glade to see you


print(a1.class_method())

#This kind of Homosapiens


print(a1.static_method())

"Something message"