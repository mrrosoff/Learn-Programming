
if __name__ == "__main__":

    # You can use the type function to see the type of a variable

    print(type("This is a String"))
    print(type(4))
    print(type(2.75))

    # You can use "Casting" to change the type of a variable

    # For example -> from String to int

    anInt = int("6")
    print(type(anInt))

    # For example -> from int to String

    aString = str(4.396)
    print(type(aString))

    # Careful with -> float to int, look what happens!

    aSecondInt = int(4.396)
    print(aSecondInt)

    # Is something like this possible?

    aBoolean = bool("True")
    print(aBoolean)
