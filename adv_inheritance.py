# inheritance in python: Single inheritance, multiple inheritance, hybrid inheritance

# single or basic inheritance

# base class 
class Parent():
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}.")
    
# derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Creating instance of a child class
child = Child("Jishnu")
child.greet() # output: Hello, my name is Baby.
child.play() # output: Baby is playing.