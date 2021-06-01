
if __name__ == "__main__":

    # The topic of this file is slicing, which means getting several elements of a String or List
    # While primarily used on Lists, as we have not learned lists, this will use Strings as a demonstration

    aString = "This is a String"

    # Slicing is inclusive on the left side but not on the right side, this is a standard of logic

    # What does this print?, Does this make sense?

    print(aString[0:4])

    # Another example

    print(aString[2:len(aString)])

    # You can also replicate the above example of "to the end", by leaving out the right side

    print(aString[2:])

    # The same is true for the left side

    print(aString[:4])

    # What does this do?, Does this make sense?

    print(aString[:])

    # Play around with slicing here!
