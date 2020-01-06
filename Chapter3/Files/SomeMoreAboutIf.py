
if __name__ == "__main__":

    aFalseVariable = False
    aTrueVariable = True

    # Sometimes you will have written the most beautiful if condition, but then you realize that what you wanted was
    # actually the opposite of what you wanted...

    # The solution is the not keyword!

    if not aFalseVariable:

        print("Opposites Attract ;P")

    # Sometimes you will want to check if two things are true, use the and keyword...

    if aTrueVariable and True:

        print("The above must BOTH be true!")

    # What if we need just one of them to be true?

    if aTrueVariable or aFalseVariable:

        print("Just one of these needs to be true!")

    # We also need to know how to check equality...

    if 5 == 10 - 5:

        print("Well I guess math still works!")

    # Not equal?

    if not (5 == 10 - 4):

        print("Sure but isnt this a bit contrived?")

    if 5 != 10 - 4:

        print("Much better...")

    # See if something is in a list or string?

    if "s thi" in "Does this work?":

        print("Well that is pretty cool")

    # Not in????

    if 5 not in [1, 2, 3, 4]:

        print("Cool!")

    # The thing to take away is that Python is VERY abstract. Talking aloud is almost akin to what you should program,
    # so just think about what you would say in a day to day conversation, and go from there!
