'''
Test 2:

Example of the "pybug.error(Exception)" function

Creates a "Dog" class with the "bark" method
A "Dog" instance, called "dog" is created
The "meow" method is called on the "dog" instance of "Dog"
An "Exception" is raised because the "Dog" object has no "meow" method
In this script however, instead of pybug finding the error on it's own, you have already found where the error is
You pipe this "Exception" into the "pybug.error(Exception)" function
PyBug then will find links related to this kind of issue and print them in the terminal when the scipt is run
'''

import pybug

class Dog:

    def __init__(self, name):

        self.name = name

    def bark(self):

        print('Bark')

dog = Dog('Normal Dog')

try:

    dog.meow()

except Exception as e:

    pybug.error(e)