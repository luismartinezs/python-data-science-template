"""class ClassName:
    # Constructor and methods here
    pass  # 'pass' can be used to create an empty class
"""


class Dog:
    # Functions that operate on an instance of the class
    # always take self as the first parameter, representing the instance
    def bark(self):  # Instance method
        return "Woof!"


# Creating an object (instance) of the class
my_dog = Dog()
print(my_dog.bark())  # Output: Woof!


class Dog:
    # constructor method is called automatically when an object is created
    # always take self as the first parameter, representing the instance
    def __init__(self, name, breed):  # Constructor to initialize attributes
        self.name = name
        self.breed = breed

    def bark(self):  # Instance method
        return f"{self.name} says Woof!"


# Creating an object with attributes
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Output: Buddy says Woof!


class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):  # Dog class inherits from Animal
    def speak(self):  # Method overriding
        return "Woof!"


# Create instances of Animal and Dog
generic_animal = Animal()
my_dog = Dog()

print(generic_animal.speak())  # Output: Animal sound
print(my_dog.speak())  # Output: Woof!


# Special Methods (__init__, __str__, __repr__, etc.)

"""
__init__: The constructor, as explained earlier, initializes the object's attributes.

__str__: Defines the string representation of an object when print() is called on it.

__repr__: Defines the "official" string representation of an object, used mostly for debugging and development.

The __str__ method provides a user-friendly description, while __repr__ is more formal and useful for debugging
"""


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"


my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog)  # Output (from __str__): Dog: Buddy, Breed: Golden Retriever
print(
    repr(my_dog)
)  # Output (from __repr__): Dog(name='Buddy', breed='Golden Retriever')


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"This is a {self.make} {self.model} from {self.year}")


my_car = Car("Toyota", "Corolla", 2020)
my_car.description()  # Output: This is a Toyota Corolla from 2020


class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "drives"


class Boat(Vehicle):
    def move(self):
        return "sails"


car = Car()
print(car.move())


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"


book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(book)  # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald, Pages: 180
print(
    repr(book)
)  # Output: Book(title='The Great Gatsby', author='F. Scott Fitzgerald', pages=180)
