
# Lets say I made the following class


class Counter:

    a = 10

    # This method declares that this object can be used as an iterator. What does that mean?

    def __iter__(self):

        return self

    # This method indicates how to proceed to the next iteration

    def __next__(self):

        if self.a < 20:

            # It is customary to return the previous value when stepping through an iterator

            x = self.a
            self.a += 1
            return x

        # We can't iterate forever, that would be bad. Using an if condition we can know when to stop...

        raise StopIteration


# Lets Test it out! Using the built in methods iter and next, we can step through our iterator...

aCounter = Counter()
aCounterIterator = iter(aCounter)

print(next(aCounterIterator))
print(next(aCounterIterator))
print(next(aCounterIterator))
print(next(aCounterIterator))

# Why is that useful? Check this out!!

for i in aCounterIterator:

    print(i)

# We have just hacked the for loop! This is suuuuuuper powerful. Play around with it and see where it takes you!
