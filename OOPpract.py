#Encapsulation  _ for private, __ for protected
#Abstraction - model real life object
#Inheritance
#Polymorphism - többalakúság   list of objects ĐCat1,Dog,Cat2,] for i in animals : animals.talk()


#classmethod,static,instance
#constructor / initializer















class Animal:
    x="sonka"
    def __init__(self):
        self._legs=4

    def _can_fly(self):
        raise NotImplementedError("superclass")

class Person(Animal):
    def __init__(self,number):
        self.number=number

        self.pet=Animal()
        
    def can_fly(self):
        print("Yay, I can fly")

    def ability(self):
        print("I have an ability")


class Student(Person):
    def __init__(self,number):
        super().__init__(number)

    def can_fly(self):
        super().can_fly()
        print("I can swim as well")

    def ability(self):
        print("I don't have an ability'")
