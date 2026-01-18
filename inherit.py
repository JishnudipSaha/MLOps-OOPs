class Animal:
    def __init__(self, name):
        self.name = name
    
    def action(self):
        print(f'{self.name} is in action')
    
    def nameOfAnimal(self):
        print(f'The name is {self.name}')

class Dog(Animal): # Animal class is inherited by Dog
    def action(self):
        print(f'{self.name} is barking')

dog = Dog('Doggesh')
dog.action()  # Doggesh is in action
dog.nameOfAnimal() # since Dog inherits Animal, so Dog class now have all the methods of Animal class
