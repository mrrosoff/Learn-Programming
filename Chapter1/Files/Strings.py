
# The main method

if __name__ == "__main__":

    # Strings are one of the most versatile variables in Python

    aString = "This is a String"

    # In Python you can declare Strings with either " or '
    # Use ", it is better practice across languages

    anotherString = 'Another String'

    # You can access a character in a String using its corresponding index
    # Indexing in a Computer starts at Zero!

    # ---- Index -> 012345
    aThirdString = "012345"

    # Print the Character at Index 0 of aString, note the square brackets

    print("aString at 0: ", aString[0])

    # Another Example, why does it print nothing?

    print("anotherString at 7: ", anotherString[7])

    # You can see how many characters are in a String by using the len() function

    print("The length of aThirdString is: ", len(aThirdString))

    # Strings also have methods inside of them you can access with the dot, for example,
    # You can get the first index of a character using the index function

    print("The index of 't' is: ", aString.index("t"))

    # You can combine Strings by doing addition!

    aThirdString = aString + anotherString

    print(aThirdString)

    # What would print if you asked for the index of a character that is not in the String?

    # Erase this and add a print statement to do that here

    # How would you print out the last character in a String, regardless of how long the String is?

    # Erase this and add a print statement to do that here

    # What happens if you ask for the character at an index that is out of range?

    # Erase this and add a print statement to do that here

