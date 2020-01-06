
if __name__ == "__main__":

    # So for loops are cool. Most of the time we will want to loop over a container like a list or a string. But
    # sometimes we want to be old school. Add up all the numbers from 1 to 1000. Like our while loop example...

    # For loops iterate over lists right? So how can we generate a list from 1 to 1000? With the range function
    # of course!

    aSum = 0

    for i in range(1000):

        aSum += i

    print(aSum)

    # This is analogous to our while loop example. AND SO MUCH PRETTY!!!
    # What we should take away from this is that the while loop, while fine, doesnt to Python justice. THE ONLY TIME YOU
    # SHOULD SEE WHILE LOOPS IN PYTHON CODE ARE IN WHILE TRUE CONDITIONS. (If you dont know what that means, dont worry,
    # we will get there!)

    # Write some code here that finds the sum of all even numbers from 1 to 100. But without the ones divisible by 5.
    # (Hint: what does the modulo operator (%) do? Perhaps google it if your own tests are inconclusive?)
