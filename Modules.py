'''
Modules in Python 
A module in Python is simply a Python file (.py) containing code—functions, variables, classes, etc.—that you can reuse in another Python program.
Module = reusable Python file

#The import Statement :
In Python, the import keyword has been provided to load a Python object from one module.
The object may be a function, class, a variable etc.
If a module contains multiple definitions, all of them will be loaded in the namespace.

#The from ... import Statement:
The import statement will load all the resources of the module in the current namespace. 
It is possible to import specific objects from a module by using this syntax. 
For Example :from Calculator import add,subtract

#The from...import * Statement:
It is also possible to import all the names from a module into the current namespace by using the following import statement.
This provides an easy way to import all the items from a module into the current namespace; however, this statement should be used sparingly.

#The import ... as Statement:
You can assign an alias name to the imported module.
The alias should be prefixed to the function while calling. 
Example : import Calculator as cal 
          print(cal.add(a,b)) '''

#For example: Calculator.py  
#can contain 

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

#Then another file can use those functions.
#Now create another file: main.py

#Import the module: 
import Calculator

print(Calculator.add(10, 20))
print(Calculator.subtract(20, 5))
print(Calculator.multiply(5, 4))  
print("File:",Calculator.__file__)

'''Output:
30
15
20   '''