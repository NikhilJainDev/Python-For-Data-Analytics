# Question 1_) WAP to display person Name, Age , and Program in three Different lines
from fontTools.misc.plistlib import end_integer

a = (""" Name : Nikhil Jain 
 Age : 20
 Address : Poornima College of Engineering , Jaipur(Rajasthan), 302022 """)
print(a)

# Question 2) write a Program to swap two variables

x = 10;
y = 20;
print("Before Swapping -> value of x is 10 and y is 20")
p = x;
x = y;
y = p;
print(f" After Swapping -> Value of x is : {x} and Value of y is : {y}")

# Question 3) Conversion of float in int value

num = float(input("Enter a Number : "))
print(num)
print(f" Conversion in int is : {int(num)}")

# Question 4) Take details from student for ID card and print in different Lines
Name  =  str(input(" Enter Your Name : "))
Age   =  int(input(" Enter Your Age  : "))
Ph_no = int(input(" Enter Phone Number : "))
Disability_status =str(input("Disabled ? Yes / No "))
Blood_Group = str(input(" Enter Blood Group : "))
College =  str(input(" Enter College Name : "))

print(" ------------------------ Student Information is ------------------------")
print(f" Name of Student -> {Name}")
print(f" Age of Student  ->  {Age}")
print(f" Ph_no of student -> {Ph_no}")
print(f" Disabled Status : {Disability_status}")
print(f" Blood of Student -> {Blood_Group}")
print(f" College Name : {College}")
print(f" -----------------------------------------------------------------------")





