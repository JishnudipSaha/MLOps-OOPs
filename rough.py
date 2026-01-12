lst = [1,2,3]
my_str = "MLOps"
my_int = 125

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

# a = "x"
# b = "y"

# print(a + b)


from oops_proj import chatbook

# user1 = chatbook()

lst = [1,2,3]

# functions - it's a standalone(not inside the class)
a1 = len(lst)  # --> it's a function
print(a1)

# method - it's not a standalone(a function that is inside the class)
user1 = chatbook()
user1.sent_msg()  # --> it's a method