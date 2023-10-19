"""
Working with Lists, Tuples, and Dictionaries
Lab overview
In Python, string and numeric data types are often used in groups called collections. 
Three such collections that Python supports are the list, the tuple, and the dictionary.
In this lab, you will:
Use the list data type
Use the tuple data type
Use the dictionary data type___
"""
# Exercise 1: Introducing the list data type
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

# Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

# Exercise 2: Introducing the tuple data type
# Defining a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Exercise 3: Introducing the dictionary data type
# Defining a dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
