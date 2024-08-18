class Animals:
    def __init__(self, name):
        self.name = name
    
class Cat(Animal):
    def speak(self):  
        return f"{self.name} meows."