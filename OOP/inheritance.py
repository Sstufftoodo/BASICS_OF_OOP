# Inheritance : Allows a class to take or inherit attributes and methods
#               from another class.
# super()     : Allows you to extend the functionality of the
#               inherited methods

class Animal:
    def __init__(self, name, can_eat, can_sleep):
        self.name = name
        self.can_eat = can_eat
        self.can_sleep = can_sleep
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Cat(Animal):
    def __init__(self, name, can_eat, can_sleep, has_nine_lives):
        super().__init__(name, can_eat, can_sleep)
        self.has_nine_lives = has_nine_lives

class Dog(Animal):
    def __init__(self, name, can_eat, can_sleep, loyal):
        super().__init__(name, can_eat, can_sleep)
        self.loyal = loyal

cat = Cat("alex", True, True, True)
dog = Dog("douglas", True, True, True)

cat.sleep()
dog.eat()