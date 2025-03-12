
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

person1 = Person("Alex Johnson", 30, "Maple Street 42")

person1.display_info()

