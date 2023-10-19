"""
Working with Conditionals
Lab overview
A section of code that compares two pieces of information is called a conditional statement.
You can use conditionals to create different paths through the program. 
Using comparative operators, you will write a program that makes decisions.

In this lab, you will:

Use the if statement
Use the else statement
Use the elif statement
"""
# Exercise 1: Working with the if statement
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")

else:
    print("Please come back when you need to ship a package. Thank you.")
    
# Exercise 3: Working with the elif statement
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

