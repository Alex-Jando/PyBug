# PyBug
*The all-in-one Python debugging solution*
#
## Features
- Points out errors in your Python scripts
- Finds articles that can help you solve the error
- Allows you to search for articles related to any question you may have

## Installation / Setup
- Install **PyBug** using pip by typing `pip install pybug` in your terminal
- Open a new python file once **PyBug** is installed
- At the begining of the file type the following:
```
import pybug
pybug.init(__file__)
```
- `__file__` can be replaced with `sys.argv[0]` or `sys.executable` to make **PyBug** work with pyinstaller
- Once you've done that **PyBug** is completely installed
- If you ever want to stop **PyBug**, you can simply just comment out `pybug.init(__file__)`
- If you want to keep **PyBug** running but you don't want to see the links, change `pybug.init(__file__)` to `pybug.init(__file__, debug = False)`

## Using **PyBug**
- **PyBug** is very simple to use, and for the most part, just runs in the background
- **PyBug** has three main functions
  - `init(__file__)` which just makes **PyBug** run when the file starts
  - `search(query)` which takes a query and will return a list of useful links related to your query
  - `error(error)` which will take an `Exception`, then find useful links related to it
  
## Contribute
- Please feel free to contribute by forking and adding any features you want
- Also if you have any ideas that you want to add, but don't know how comment it somewhere
