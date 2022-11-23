
if __name__ == "__main__":

    # Say we want to add all the numbers up between 1 and 1000. We could type all the numbers into a calculator, but
    # This would take a very long while. This is what computers were designed to replace.

    # A Basic Loop has three parts.
    # 1. The Counter
    # 2. The End Condition
    # 3. The Operation

    # Start by declaring the counter.

    counter = 1

    # This variable will keep track of our sum

    theSum = 0

    # Then add the end condition. Note the colon and lack of parenthesis.

    while counter < 1000:

        # Note the indentation here. This is the 'operation' step. What does this line do?

        theSum = theSum + counter

        # If you are confused, uncomment this line

        # print(sum)

        # Make sure you increment the counter. Notice the syntax of this line. This is analogous to the line above.
        # Less Typing = Better

        counter += 1

    # Note the indentation of this line. We are now 'out' of the loop.

    print(theSum)

    # Fill in a method above that returns the value of n! given n as a parameter. Think about how you could use a loop
    # to achieve a multiplication from 1 to n. Test code is provided

    # print('Should return 6: ', factorial(3))
    # print('Should return 24: ', factorial(4))
    # print('Should return 120 ', factorial(5))
