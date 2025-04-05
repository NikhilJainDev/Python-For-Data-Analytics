
a = str(input(" Enter Your Name here : "))
print(len(a))
print(f" The type of variable a is : {type(a)}")

# Strings : Anything that is written inside the double quotes is called Strings

# b = "Jain"
# b[2] = "p"
# print(b)
 # Strings are immutable in Python

data = ["Nikhil" , "Saloni", "Suyash", "Muskan", "Abhay", "Mayurakshi", "Aarohi", "Vibhor"]
print("------------------ Before Modification -----------------------")
print(data)
data[2] = "Kamal"
data[4] = "Suman"
print("----------------- After Modification -----------------------")
print(data)
# Lists are Mutable in Python

z = 5+3j
print(f" The Type of z is : {type(z)}")
print(f" The Real Part of {z} is : {z.real}")
print(f" The Imaginary Part of {z} is : {z.imag}")


p = str(input(" Enter a Expression : "))
print(p)

# 'Eval' data type is used to evaluate the value along with the string 
q = eval(input(" Enter a Expression : "))
print(q)

