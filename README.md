Basic OOP Example in Python
This repository contains a simple example of Object-Oriented Programming (OOP) in Python. It demonstrates the core concepts of OOP, including classes, objects, attributes, and methods.

Code Overview
The code defines a Dog class with:

Class Attribute: species (shared by all instances of the class).

Instance Attributes: name and age (unique to each object).

Methods: bark() and get_age() (functions that operate on the object).

Example Code
python
Copy
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
How to Run the Code
Clone this repository:

bash
Copy
git clone https://github.com/hadi95383/basic-oop-python.git
Navigate to the repository directory:

bash
Copy
cd basic-oop-python
Run the Python script:

bash
Copy
python dog_example.py
Output
When you run the script, you should see the following output:

Copy
Buddy
Canis familiaris
Buddy says woof!
Max is 3 years old.
Key OOP Concepts Demonstrated
Class: A blueprint for creating objects (e.g., Dog).

Object: An instance of a class (e.g., dog1 and dog2).

Attributes: Variables that belong to an object or class (e.g., name, age, species).

Methods: Functions that belong to an object or class (e.g., bark(), get_age()).

Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. All contributions are welcome.
