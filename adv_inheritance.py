# inheritance in python: Single inheritance, multiple inheritance, hiarchical ineritance, hybrid inheritance

# # single or basic inheritance

# # base class 
# class Parent():
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}.")
    
# # derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # Creating instance of a child class
# child = Child("Jishnu")
# child.greet() # output: Hello, my name is Baby.
# child.play() # output: Baby is playing.

#---------------------------------------------------------

# # Multi-level inheritance


# class GrandParent():
#     def __init__(self, name):
#         self.name = name
#     def tell_story(self):
#         print(f"{self.name} is telling a story.")

# class Parent(GrandParent):
#     def work(self):
#         print(f"{self.name} is working.")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # creting instance of child
# child = Child("Jisnudip")
# child.tell_story() # output: Jisnu is telling a story.
# child.work() # output: Jishnu is working.
# child.play() # output: Jisnu is playing.

#---------------------------------------------------------

# Hiarchical inheritance

# # base class 
# class Parent():
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"{self.name} is greeting.")

# # derived class 1
# class ChildOne(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")
        
# # derived class 2
# class ChildTwo(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# # creating objects of clid classes

# child1 = ChildOne("Jisnudip")
# child2 = ChildTwo("Aritra")

# child1.greet() # output: Jishnudip is greeting.
# child1.play() # output: Jishnudip is playing.

# child2.greet() # output: Aritra is greeting.
# child2.study() # output: Aritra is studying.

#--------------------------------------------------------

# Multiple inheritance (Diamond problems)

# # base class
# class A:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# # intermediate class 1
# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# # intermediate class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()
        
# # derived class
# class D(B, C):
#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# # creating instance of D
# d = D("Jishnu")
# d.greet()
# '''
# output:
# Hello from D, Jishnu
# Hello from B, Jishnu
# Hello from C, Jishnu
# Hello from A, Jishnu
# '''

#----------------------------------------------------------------------

# Hybrid Inheritance

# base class
class Animal():
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print(f"{self.name} makes a sound.")

# intermediate class 1 (Hiarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)
    
    def nocturnal(self):
        print(f"{self.name} is a nocturnal.")

# creating instance of a bat
bat = Bat("Binod")
bat.sound() # output: Binod makes a sound
bat.feed() # output: Binod is feeding milk.
bat.fly() # output: Binod is flying.
bat.nocturnal() # output: Binod is nocturnal.