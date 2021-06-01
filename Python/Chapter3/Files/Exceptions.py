
# Here is a script without a main method...

try:
    print(x)
except:
    print("An exception occurred")

# We tried to run the code print(x), but x was not defined. It should have crashed with an error you say!
# Well, we caught the exception and printed our own error message!

# Generally, a general except is a bit too broad... So here is a typed error clause...

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# This type of error handling is the best kind. In the event of an error, it is best to simply print what went wrong
# and continue to run our code. Crashing our entire program is usually not a great option.

# Just because there is no main method doesnt mean it wont run. So why go through all the trouble of __main__ then?

# Because it is good practice. And others who read your code will understand it.
