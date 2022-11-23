
# Say we wanted to write a method that returns whether a number is less than 10. We would write a method like so.

def lessThanTen(aNumber):

    return aNumber < 10

# This is great, but what if we wanted to see if one number is less than some other number. You might write this:

def lessThan2ndParameter(numberOne, numberTwo):

    return numberOne < numberTwo

# This works! What if we then wanted to say "IF" this method returns true, we should do something, otherwise, give up.

if __name__ == "__main__":

    # An if condition allows us to do just this. For example: Start by reading two numbers in.

    numberOne = int(input("Enter a number: "))
    numberTwo = int(input("Enter a second number: "))

    # Then see what the method returns!

    booleanResult = lessThan2ndParameter(numberOne, numberTwo)

    # The if condition. If it is true, print. Notice the indentation and lack of parenthesis.

    if booleanResult:

        print(numberOne, "is less than", numberTwo, "!")


    # If conditions take booleans as their arguments, so it is logical to simplify the above to ->

    if lessThan2ndParameter(numberOne, numberTwo):

        print(numberOne, "is less than", numberTwo, "!")

    # We can add an alternate condition by using elif

    elif numberOne == 5:

        print(numberOne, "is equal to 5. Would you look at that")

    # We can add a condition to run if all of the above conditions return false... (the default case)

    else:

        print(numberOne, "is greater than", numberTwo, "!")

    # Now try writing your own method above. Call it squares. It should take two parameters and return true if and only
    # if the square of the first number is equal to the square root of the second. In addition, if the method would
    # return false, print out the difference between the square of the first number and the square root of the second
    # number. Test code is provided here ->

    # print("This should return True: ", squares(2, 16))
    # print("This should return False and print 4 before this: ", squares(2, 64))