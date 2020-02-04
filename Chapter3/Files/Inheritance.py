
# I am going to borrow our Person class.


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def wave(self):

        print("Hello my name is " + self.name)


# What if I wanted to make a subset of people, perhaps students?

# Here is a class, Student, that inherits all of the properties of Person

class Student(Person):

    # It has its own init function that overrides that of its parent

    def __init__(self, name, age, idNumber):

        # The super function uses the parents class to call. So this line calls the parent class's init method.

        super().__init__(name, age)
        self.idNumber = idNumber


# Lets Test

aStudent = Student("Max", 20, 12345678)

aStudent.wave()
print(aStudent.idNumber)

# Seems to work!
