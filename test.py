import pybug

pybug.init(__file__)

class Dog:

    def __init__(self, name):

        self.name = name

    def bark(self):

        print('Bark')

Jinja = Dog('Jinja Jando')

Jinja.meow()