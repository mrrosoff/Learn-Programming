
# Tuples are like lists... Except they cant be changed.

if __name__ == "__main__":

    aTuple = (1, 3, 7)
    anotherTuple = ("This", "is", "a", "tuple!")

    print(aTuple, anotherTuple)

    # There is a hack however

    temp = list(aTuple)
    temp.append(4)
    aTuple = tuple(temp)

    print(aTuple)

    # Yay! We hacked tuples. Tuples are worthless... Use lists...
