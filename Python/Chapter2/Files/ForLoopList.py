
if __name__ == "__main__":

    # A for loop is the primary reason to use Python. It is beautiful. It is elegant. It makes me happy and it should make
    # you happy too. The for loop in Python is infinitely versatile.

    aList = [1, 2, 3, 4, 5]

    # Here is a for loop that prints out a list. Notice the indentation and the 'in' keyword. 'item' is just some name
    # I made up. Use your own names that make sense!

    for item in aList:

        print(item, end=", ")

    print()

    # Here is another for loop. What do you think it will print?

    for item in "This is a String":

        print(item)

    print()

    # Pretty Cool Huh? Try playing with for loops here then keep going!





    # Python Lists are infintely flexible containers. What does THIS do??????

    anotherList = [item for item in aList]

    print(anotherList)

    # WHAT!!! This is amazing. We can wrap for loops inside lists! (For the CS folks, not only is this pretty, but it
    # actually gets optimized interpreter side and results in significantly faster code through inlining! WOW!)

    # Try adding each character in a String variable to a list using an inline for loop like the one above here!
