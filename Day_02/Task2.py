


'''
Data Types

Learn about the primitive data types in Python.

Strings
Integers
Floats
Booleans
'''
'''
len("Hello")
word = "Hello"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
'''


print("123" + "456")
print(123+456)
print(3.14)
print(True)
print(False)

#Solution
# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)


'''
Type Error, Checking and Conversion

TypeError
These errors occur when you are using the wrong data type. e.g. len(12345)

Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

PAUSE 1. Fix the len() function so it has no more warnings or errors.
Type Checking
You can check the data type of any value or variable in python using the type() function.

print(type("abc")) #will give you <class 'str'>

PAUSE 2. Write out 4 type checks to print all 4 data types
Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>

Type Conversion
You can convert data into different data types using special functions. e.g.

float()

int()

str()

PAUSE 3. Make this line of code run without errors
print("Number of letters in your name: " + len(input("Enter your name")))

'''
#len(12345)

'''
print(len("12345"))
print(type("12345"))
print(type(12345))
print(type(3.14))
print(type(True))
'''

#print(int("123") + int("456"))


print("Number of letters in your name: " + str(len(input("Enter your name"))))

#Solution
# TypeError
# len(123)

# No TypeError
len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))







'''
Mathematical Operations

Basic Operators
Learn to use the basic mathematical operators, +, -, *, /, // and **

PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

PAUSE 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)

PAUSE 2. Change the code so it outputs 3?
print(3 * 3 + 3 / 3 - 3)

'''
# print("My age: " + str(12))
# print(6+100)
# print(100-6)
# print(3*2)
# print(6/4)
# print(6//4)
# print(2**3)

print(3 * 3 + 3 / 3 - 3)

#Solution
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# PEMDASLR Order
# ()
# **
# * OR /
# + OR -

# Outputs 7
print(3 * 3 + 3 / 3 - 3)

# Outputs 3
print(3 * 3 + 3 / 3 - 3)


'''
Number Manipulation

Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

int(3.738492) # Becomes 3

Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14

Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

+=

-=

*=

/=

f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")

# Will output I am 12 years old.


'''

# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi))
# print(round(bmi, 2))
from abc import ABC

# score = 0
# score -= 1
# print(score)
#
# print(f"Your score is {score}")


S1 = 000
S2 = 123
S3 = 456

print(f"First name is {S1} and second name is {S2} and third name is {S3}")

#Solution

bmi = 84 / 1.65 ** 2

# Original Float with decimal places
print(bmi)

# Flooring the number by converting it into int
print(int(bmi))

# Rounding the number into a whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi, 2))


## Accumulate
score = 0

# User scores a point
score += 1
print(score)

#Also
score -= 1
score *= 2
score /= 2

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")





'''
Tip Calculator Project

We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60

Demo
https://appbrewery.github.io/python-day2-demo/

Very Optional Reading: Floating Point Arithmetic
https://docs.python.org/3/tutorial/floatingpoint.html

'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


total = bill + bill*tip/100
Divided_share = round(total/people, 2)

print(f"Each person should pay: ${Divided_share}")


#Solution
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

