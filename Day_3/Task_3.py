
'''
If Else

Condition Check
Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. e.g.

if <this condition is true>:

    <then execute this line of code>

What if the condition is false?
The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.

if pigs can fly:

    <Some code that will never execute>

else:

    print("This is real life")

Python Indentation
Understand the importance of indentation in Python as a way to make certain lines of code subsidaries of other lines of code.

e.g.

if 5 > 2: #This is a parent line of code

    print("yes") #this is a child line of code

Comparator Operators
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to

'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("No rollercoaster!")

#Solution 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")



'''
Modulo


The modulo operator gives you the remainder of a division.

6 % 2 #will be 0

6 % 5 #will be 1

6 % 4 #will be 2

PAUSE 1 - What is 10 % 3?
What do you think this will output?

print(10 % 3)

PAUSE 2 - Check Odd or Even
Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

 Hint 
1. First get the user input using the input() function.
2. Next, convert the input into an int using the int() function.
3. Now store the number in a variable.
4. Use the modulo (%) to check if the user input number can be divided cleanly by 2.
5. Use if/else to check if the result of the modulo check in step 4 is equal to 0 then that input number is even, otherwise it's odd.


'''

number = int(input("What is your number?"))

if number <= 0:
    print("Enter a valid positive number")
else:
    if number % 2 == 0:
        print("The number is Even")
    else :
        print("The number is Odd")


#Solution
number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")




'''
Nesting and Elif

You can put if/else statements inside other if/else statements. This is known as nesting. e.g.

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english)
In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

Note: You can also have if statements that don't have a paired else statement.

'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
Photo = bool(input("Would you like to see the photo? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <=12:
        if Photo == True:
            print("Please pay $8")
        else:
            print("Please pay $5")
    elif age <= 18:
        if Photo == True:
            print("Please pay $10")
        else:
            print("Please pay $7")
    else:
        if Photo == True:
            print("Please pay $15")
        else:
            print("Please pay $12")

else:
    print("Sorry you have to grow taller before you can ride.")



#Solution 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")



'''
Multiple Ifs

You can write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:

# If/elif/else
if <condition 1 is true>
    <do A>
elif <condition 2 is true>
    <do B>
else
    <do C>
# Nested if statements
if <condition 1 is true>
    <do A>
    if <condition 2 is true>
        <do B>
        if <condition 3 is true>
            <do C>
# Multiple if statements
if <condition 1 is true>
    <do A>
if <condition 2 is true>
    <do B>
if <condition 3 is true>
    <do C>
In the if/elif/else block, only one of A, B, or C can happen, because if/elif/else are mutually exclusive. The first condition has to fail to go into the elif and the elif (or multiple elif) have to fail to go into the else. Condition 2 is only checked if condition 1 is false.

In the nested if statements, A, B and C can all happen, but conditions 1, 2 and 3 must all be true. The computer will only check condition 2 if condition 1 is true.

In the multiple if statements, A, B, and C can all happen. But they are completely independent of each other. C can happen even if A and B don't. Every condition is checked, no matter the result of the others.

'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")



#Solution
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")



'''
Python Pizza

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Interaction
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.
 Hint 
Don't change any of the starting code and make sure that the final sentence says "Your final bill is: $." including the full stop and the same wording. Otherwise, the tests will not pass.

'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L" :
    bill = 25
else:
    print("Sorry you have to enter S, M, or L.")

if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill += 3

if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is: ${bill}.")


#Solution
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


'''
Logical Operators

You can combine different conditions using logical operators.

A and B #Both conditions need to be true
C or D #Only one condition needs to be true
not E #The condition must be false

PAUSE 1 - Age 45 to 55 Modifier
Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than 45, and it's also less than 55.

NOTE: The warning for simplification is just a suggestion. You can consider it and chose it, or you can ignore it. In this lesson I wanted to show you the and, or and not logical operators. So I recommend keeping the original code in case you come back to this lesson for review.

'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >18 and age < 45 :
        bill = 12
        print("Adult tickets are $12.")
    elif age >= 45 and age <=55:
        mlbill = 0

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    if age < 45 or age >55:
        print(f"Your final bill is ${bill}")
    else:
        print("Its your free ride")

else:
    print("Sorry, you have to grow taller before you can ride.")


#Solution
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        # Or
        # 45 <= age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")



'''
Treasure Island Game

Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart linked here to create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!

 Hint 
You can use the lower() function to turn any string into all lower case. https://www.w3schools.com/python/ref_string_lower.asp
Alternatively you can also use the logical operator "or" to check for other spellings of user choice. e.g. Right, right or RIGHT.

Demo
https://appbrewery.github.io/python-day3-demo/


'''

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
d1 = input("Left or Right?")

if d1 == "Left":
    d2 = input("Swim or Wait?")
    if d2 == "Wait":
        d3 = input("Which door do you choose? Red, Blue, Yellow.")
        if d3 == "Yellow":
            print("You win!")
        elif d3 == "Red":
            print("You just got burned by a Wildfire. GAME OVER")
        elif d3 == "Blue":
            print("You got eaten by beasts. GAME OVER")
        else :
            print("GAME OVER")
    else:
        print("You got attacked by a trot. GAME OVER")
else:
    print("You fall into a hole. GAME OVER")


#Solution

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")
