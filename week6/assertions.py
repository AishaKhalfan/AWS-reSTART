# Assertions are conditions, such as ifstatements, that check the values in the application•
# Dynamic analysis uses assertion statements during runtime to raise errors when conditions certain conditions occur.•As an example consider the following function.  
# The developer wants to ensure that the age value is always a positive number greater than zero.  The following assertion checks this:

def loguserage(age):
    age = int(input("what is your age? "))
    assert age <= 0, "Invalid age was supplied"
