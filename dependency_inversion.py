# imports
from abc import ABC, abstractclassmethod


# Dependency Inversion = Hight Level Module should not depend on low level module, but both should depend on abstractions.
# Abstractions should not depend on details, but details should depend on abstractions.


# The Below example is tightly coupled both high level module and lower level module.
class Cookie:
    def bake(self) :
        print("cookie is baking")

class Bread:
    def bake(self) :
        print("Bread is baking")

class Cook:
    # Here we bake and cook the food.
    def __init__(self) :
        self.cookie = Cookie()
        self.bread = Bread()
    
    def prepare(self, item: str) :
        if item == "cookie" :
            return self.cookie.bake()

        if item == "bread" :
            return self.bread.bake()

if __name__ == '__main__' :
    pass
  #  cook = Cook()
  #  cook.prepare("cookie")
    
     
# to solve the high coupling beteween the dependent class and dependency class we can use the
# dependency inversion

# creating a interface 
class Bakable(ABC):
    @abstractclassmethod
    def bake(self):pass

class Cookie(Bakable):
    def bake(self) :
        print("Cookie is baking")

class Bread(Bakable):
    def bake(self):
        print("Bread is baking")

class Cook:
    def prepare(self, bakable : Bakable) :
        return bakable.bake()



if __name__ == "__main__" :
    cookie = Cookie()
    bread = Bread()
    cook = Cook()
    cook.prepare(bread)