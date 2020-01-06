
# A method is a tiny program inside a bigger program

# To declare a method, start with the def operator, then write the name of the method, then parenthesis
# Make sure you include a colon!
# It is traditional to follow the following naming convention when naming methods, remember to start with lowercase
# similar to variables!

def methodOne():

    print("I am in methodOne!")


# You can also use a method to send information back to the callee, do this with the return keyword

def methodTwo():

    return "I am from methodTwo!"


# Remember this is the main method -> It has a special format

if __name__ == "__main__":

    # Note how you call a method. Simply use the name with parenthesis

    # methodOne will print for us, so we can just call it

    methodOne()

    # methodTwo sends us back information so we need to assign the method to a variable, or just use it immediately

    print(methodTwo())

    # or

    holdsInformation = methodTwo()
    print(holdsInformation)

    # Try declaring a method above of your own name, and have it return the value of 10 ** 2
    # print the result of calling this method here in main
