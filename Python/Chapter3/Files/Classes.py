
# This is the hardest part of Python. Just warning you.

# Here is a class. Classes can hold two things, data and methods.

class MyClass:

    x = 5
    y = 10

# To access the data in a class, we need to instantiate an object of that type.

anObject = MyClass()

# We can then access its data using the . operator

print(anObject.x)

# Can I change it?

anObject.x = 20
print(anObject.x)

# Looks like it... But what about this?

anotherObject = MyClass()

print(anObject.x, anotherObject.x)

# Both objects keep SEPERATE copies of the class data. Everyone gets their own!

# Lets define a class to represent a person.


class Person:

    # An Init method is what Python will run upon object creation. This one takes two parameters, name and age.
    # Two you say! But there are three parameters?? The first parameter in a class method is always self. This is
    # Pythons way of keeping track of who is who. Try not to let it confuse you.

    # self.name and self.age both set class variables. Similar to our above example.

    def __init__(self, name, age):

        self.name = name
        self.age = age

    # Here is a regular class method. Notice the parameter to the method being self.

    def wave(self):

        print("Hello my name is " + self.name)


# Lets test it out! I declare two people. When I declare them, I pass their names and age to the init method.
# Programmers sometimes call the init method the constructor.

me = Person("Max", 20)
jack = Person("Jack", 19)

print(me.name, me.age)
print(jack.name, jack.age)

me.wave()
jack.wave()

# It worked! This is called object oriented programming. Python wasn't really designed for it. But modern problems
# require modern solutions.

