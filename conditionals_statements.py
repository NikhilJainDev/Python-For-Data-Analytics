# # Conditional Statements -> The Statements that are used to specifies and executes when a condition happened
# # Problem 1

num = int(input(" Enter a Number : "))
if( num % 2 == 0 ):
    print(f" {num} is even ")
else:
    print(f"{num} is odd ")


# Positive / Negative or Zero

number = int(input("Enter a Number -> "))
if(number > 0):
    print(f"{number} is +ive ")
elif(number < 0):
    print(f"{number} is -ive ")
else:
    print(f"{number} is zero")

# # Leap year Program

year = int(input("Enter a Year to check Leap or not : "))
if(year % 400 == 0):
    print(f"{year} is a leap year ")
elif(year % 4 == 0 and year % 100 != 0):
    print(f"{year} is leap")
else:
    print(f"{year} is ordinary ")

# Prime Number or not
digit = int(input("Enter a digit: "))

if digit < 2:
    print(f"{digit} is not prime")
else:
    for i in range(2, digit):
        if digit % i == 0:
            print(f"{digit} is not prime")
            break
    else:
        # This else belongs to the for loop (not the if!)
        print(f"{digit} is prime")



