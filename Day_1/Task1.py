

'''
1.1 
Printing
Use what you learnt to print out the words "Hello world!" with Python code.

Then click the run button to execute your code.

 Hint 
Remember that this is the format to print things in Python: print("some text")
'''

'''
String Manipulation 
Learn to use string concatenation and the new line escape sequence to format strings in Python.

PAUSE 1. Use \n to add another line of "Hello world".
So the resulting output looks like this:

Hello world!

Hello world!

Hello world!

PAUSE 2. Add a space between the strings
So there is a space between the string Hello and Angela when the print statement runs.

The output should look like this:

Hello Angela
'''


'''
Inputs

Learn to use the Python input() function to collect user input and use it within your code.

PAUSE 1. Update the code to add an exclamation mark Using what you have learnt in this lesson and previous, can you figure out how take user input and slot it in between 2 strings?

You are looking to print a sentence like this:

Hello Name!

e.g. Hello Angela!
'''

'''
Variables

Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.

PAUSE 1. Check the length of the user input
Using what you have learnt about the len() function and the input() function. Try to print out the number of characters in the user input. Write everything in just 1 line of code.

PAUSE 2. Split everything into variables.
Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation.

'''

'''
Variable Naming

Learn the rules of variable naming in Python.

Rules
Make sure your variable names are descriptive
Don't have spaces between words
Don't start with numbers
Don't use special words like print or input
Choose simple words that are less likely to become typos
Check the company style guidelines if you start work at a company

'''

'''
Band Name Generator Project

Create a greeting for your program.
Ask the user for the city that they grew up in and store it in a variable.
Ask the user for the name of a pet and store it in a variable.
Combine the name of their city and pet and show them their band name.
 Hint 1 
You can use String Concatenation to combine strings with variables too! e.g. print("My name is " + name)
Make sure the input cursor shows on a new line:
 Hint 2 
Think about how you used \n to add a new line to a string. Try putting it in some different places in your code until it does what you expect. Note, when you click into the output area you will be able to click on the end of the line as well as the new line. See the video solution for how it looks on my system.

'''







# Write your code below this line 👇
#print ("Hell world\nHell world ")
# print(" Hello" + " CVGS")

# print("What is your name?")
# input("What is your name?")
# print("Hello" + input(" your name is ? "))

# print("Hello " + input("your name is\n") + "!")
#name = input("name? ")
#print(len(input("name ? \n")))

username = input("username please ! \n")
length = len(username)
print(length)

#name = "CVGS2"
#print(name)
