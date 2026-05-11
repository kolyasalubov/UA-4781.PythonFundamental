class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Вітаємо, {self.name}!"

    @classmethod
    def get_species(cls):
        return "Species: Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "Це довільне повідомлення від статичного методу."
person = Human("Наталія")
print(person.welcome_message())
print(Human.get_species())
print(Human.arbitrary_message())