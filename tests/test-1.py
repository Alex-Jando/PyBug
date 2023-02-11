'''
Test 1:

Example of the "pybug.init(__file__)" function

Creates a "Dog" class with the "bark" method
A "Dog" instance, called "dog" is created
The "meow" method is called on the "dog" instance of "Dog"
An "Exception" is raised because the "Dog" object has no "meow" method
PyBug then will find links related to this kind of issue and print them in the terminal when the scipt is run
'''

import pybug

pybug.init(__file__)

class Dog:

    def __init__(self, name):

        self.name = name

    def bark(self):

        print('Bark')

dog = Dog('Normal Dog')

dog.meow()