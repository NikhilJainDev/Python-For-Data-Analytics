# Variables are the containers that contains some values
from operator import truediv

a = "Hello world"
print(a)

a = 10
b = 20
print(type(a))
print(type(b))
print(type(4.2))

print(f" The sum of {a} and {b} is {a+b}")

x = {
    "Name" : "Nikhil",
    "Age" : 20,
    "Ph. No" : "8426005061",
    "Address" : "Alwar, Rajasthan",
}
print(x)
print(f" The type of variable x is : {type(x)} ")

# Iterating on a List in Python
container = ["Nikhil", 20, "Poornima College of Engineering" , "8426005061"]
print(container)

for i in range(0, len(container)):
    print(container[i])