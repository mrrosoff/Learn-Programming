
# This file is mostly for the Computer Programmers of the World. If you get lost on this file dont worry about it. Just
# ask for help!

# The method below is an example of something that is possible in Python due to the lack of type clarity on variables.
# As there is no declared return type for methods, what is stopping us from returning different types of variables in
# different situations?

# THIS IS VERY VERY BAD PRACTICE. DO NOT DO THIS. THIS WILL RESULT IN EVERYONE HATING YOU. DO ... NOT ... DO ... THIS !!

def anExample(anExampleParameter):

    if anExampleParameter < 0:

        return "This is a String"

    elif anExampleParameter > 0:

        return 100

    else:

        return False


if __name__ == "__main__":

    # Dont try to trick the system. Return one type of variable per method. Make your code EASY to read. Dont be a
    # jackass. EVERYONE WILL HATE YOU.

    print(anExample(-10))
    print(anExample(10))
    print(anExample(0))
