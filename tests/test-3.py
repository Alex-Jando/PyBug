'''
Test 3:

Example of the "pybug.search(query)" function

Creates a "Dog" class with the "bark" method
A "Dog" instance, called "dog" is created
The "meow" method is called on the "dog" instance of "Dog"
An "Exception" is raised because the "Dog" object has no "meow" method
In this script however, instead of pybug finding the error on it's own, you have already found where the error is
You print out the error and get the following result: "AttributeError: 'Dog' object has no attribute 'meow'"
You then decide to print the links in the terminal so you can check them out yourself, and see which ones migh be useful
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

    print(e)

print('Finding links:')

links = pybug.search("AttributeError: 'Dog' object has no attribute 'meow'")

[print(link) for link in links]