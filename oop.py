# 1st ex
print("1st exer..")


class Person:
    def __init__(self):
        self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print(f"Ошибка: Возраст не может быть отрицательным ({age})\n")


p = Person()
p.set_age(25)
print(f"Возраст: {p.get_age()}")
p.set_age(-5)


# 2nd ex
print("2nd exer..")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow\n"


dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())


# 3rd ex
print("3rd exer..")


class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling\n"

def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))


# 4th ex
print("4th exer..")


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592 * self.radius ** 2


rect = Rectangle(10, 5)
circle = Circle(7)

print(circle.area())
print(rect.area())
