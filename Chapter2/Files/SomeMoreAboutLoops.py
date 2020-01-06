
if __name__ == "__main__":

    # Sometimes you will be writing some loops and need to have a condition where the loop is terminated.

    counter = 0

    # This loop never terminates! How will we ever get out??

    while True:

        if counter / 10 == 2:

            # The break keyword exits whichever loop is closest in scope to it

            break

        counter += 1

    # We are free!!!! Does this number make sense?

    print(counter)

    # Here is another example of a situation you might encounter. Perhaps you are writing a loop and want to skip
    # certain iterations

    aSum = 0

    for i in range(10):

        if i % 5 == 0:

            # The continue keyword skips the current iteration and continues
            # on which ever loop is closest in scope to it

            continue

        aSum += i

    # Does this number make sense?

    print(aSum)
