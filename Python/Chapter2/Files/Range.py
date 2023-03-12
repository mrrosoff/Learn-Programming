
# In the event of a loss of a main method, the Python interpreter will execute code in whatever order it comes in.

# For example:

print('This is bad practice.')
print('Use a main method.')

# What happens if we include both? We can comment multiple lines with three quotation marks. This is called a
# 'docString'. Try uncommenting this main method and giving it a run.

"""
if __name__ == "__main__":

    print('Hello')
    
    # The purpose of this file is to teach the range function. The range function returns a generator of a list of integers. There are
    # 1 to 3 parameters to this function. A generator is a function (another name for a method) that doesnt compute all of its returned values at once, 
    # instead saving precious CPU and memory and only returning the values asked as needed. The benefits of this will become more apparent as you get deeper.
    # We can force the generator to be "unpacked" by placing a * in front of the function call.
    
    # The most basic form of the range function. This parameter acts as the final point of the list. It returns a list from 0 to n.
    # range(n)
    
    print(*range(10))
    
    # The optional second parameter allows one to specify both the beginning and the end of the list. 
    # range(n, m)
    
    print(*range(2, 10))
    
    # The optional third parameter allows one to control the 'increment' of the list. This defaults to one. 
    # range(n, m, i)
    
    print(*range(2, 10, 2)
    
    # Use the range function to print a list from 2 to 20 counting every 3.
    # How about every 5?
    # What if you make it from 2 to 25 counting every -1?
    # What if you make it from 25 to 2?
    
    # Test these here.
    
"""


