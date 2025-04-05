# Operators -> The Symbols that are used to perform some operations are called operators
from fontTools.feaLib.ast import SHIFT
from pygments.lexers.xorg import XorgLexer

# Operands ->  Variables between whom the Operation is Performing is called Operands

a = 20
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

print("---------- use of while loop in python ----------------")
i = 1  # Initialization
while(i <= 10): #condition
    print(i)
    i = i + 1 # Updation


    #  Bitwise Operators : The Operators that Compares the Binary Number

    # AND &
    # OR |
    # XOR
    # LEFT SHIFT
    # RIGHT SHIFT

print(f" Binary format of 10 is : {bin(10)}")
x = 10
y = 8
print (x & y)

print (f" The OR operation of {x} and {y} is {x | y}")

print(f" The XOR operation of {x} and {y} is {x ^ y}")