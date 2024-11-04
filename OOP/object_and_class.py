# object : A "bundle" of related attributes (variables)
#          and methods (functions)
#          Ex. phone, cup, book.
#          You need a "class" to create many objects
#
# class  : (blueprint) used to design the structure and layout of an object

class MyPhone:
    def __init__(self, model, os, is_oled, can__cure_depression):
        self.model = model
        self.os = os
        self.is_oled = is_oled
        self.can__cure_depression = can__cure_depression
    
    def turns_on(self):
        print(f"This {self.model} is turned on")
    
    def turns_off(self):
        print(f"This {self.model} is turned off")

phone = MyPhone("Realme", "Android", False, False)

print(phone.turns_on())