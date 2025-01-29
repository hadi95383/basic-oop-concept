# Define a class
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor method (initializes object attributes)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Create objects (instances of the Dog class)
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Access attributes and call methods
print(dog1.name)          # Output: Buddy
print(dog2.species)       # Output: Canis familiaris
print(dog1.bark())        # Output: Buddy says woof!
print(dog2.get_age())     # Output: Max is 3 years old.