
#Pets with legs and name
class Animal:
    def __init__(self,legs,name):
        self.legs=legs
        self.name=name
    
    def say(self):
        print("Make a sound")

class Cat(Animal):
    def __init__(self,legs,name):
        super().__init__(legs,name)
    
    def say(self):
        print("Meow")


class Oroszkek(Cat):
    def __init__(self,legs,name):
        super().__init__(legs,name)

    def say(self):
        print("Meow Oroszkek")
        print(Dog.teeth)
        
class Dog(Animal):
    teeth=0
    def __init__(self,legs,name):
        super().__init__(legs,name)
        Dog.teeth=10
        self.cat=Cat(10,"Szia")

    def get_legs(self):
        return self.legs

    def set_legs(self):
        self.legs+=1

    def say(self):
        self.cat.say()
    
    @classmethod
    def grow_teeth(cls):
        cls.teeth+=1
        
    @staticmethod
    def printer():
        print("Vau")
    
    def grow_legs(self):
        self.legs+=1

#cat=Animal(3,"Kitty")
dog=Animal(4,"Doggy")

dog.say()

