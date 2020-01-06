
# Methods are generally used to simplify code or avoid repetition.

# Here is a method which has two parameters, as in it has two variables inside the parenthesis.

def doPower(base, exponent):

    return base ** exponent

# Note a strange property of methods, parameters are COPIES of the variables, this is illustrated here.

def exampleOfCopy(aVariable):

    aVariable = 5

# Of course there is an exception, and it is lists

def exception(aList):

    aList.append("anItem")


if __name__ == "__main__":

    twoToTheFifth = doPower(2, 5)
    threeSquared = doPower(3, 2)

    print("Chapter2 to the Fifth is: ", twoToTheFifth)
    print("Chapter3 Squared is: ", threeSquared)

    showcaseVariable = 2
    exampleOfCopy(showcaseVariable)

    # You would expect this value to be 5, but it is 2

    print(showcaseVariable)

    aList = []
    exception(aList)

    # Based on above you would expect this to print [] but it prints ["anItem"]

    print(aList)
