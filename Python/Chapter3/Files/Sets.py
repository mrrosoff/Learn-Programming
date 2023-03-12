
# Sets are like lists... Except they cant be indexed. The reason for this is
# sets are internally sorted and contain only 1 of each item.

if __name__ == "__main__":

    aSet = {1, 3, 7, 7}
    anotherSet = {"This", "is", "a", "set!"}

    print(aSet, anotherSet)

    # I want to do this...

    # print(aSet[1])

    # But sets dont have indexes... Sets are for the most part worthless unless you 
    # need the "only 1 of each item property of them". Use lists instead.
