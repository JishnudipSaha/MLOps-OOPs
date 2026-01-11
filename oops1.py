#initiate a class
class Employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("This travelled function was called manually")
        print(f"Employee is travelling to {destination}")

# creating an object or instance of a class
jishnu = Employee()

# printing the attributes
# print(jishnu.salary)
# print(jishnu.id)

# calling the method
# jishnu.travel("Belgharia")
print(type(jishnu))
