'''A Python function is a block of organized, reusable code that is used to perform a single, related action.
A Python function may be invoked from any other function by passing required data (called parameters or arguments). 
The called function returns its result back to the calling environment.
Function blocks begin with the keyword def followed by the function name and parentheses ().

Types of Python Functions:
1.Built-in Functions :
Some of Python's built-in functions are print(), int(), len(), sum(), etc. 
These functions are always available, as they are loaded into computer's memory as soon as you start Python interpreter.
2.User-defined functions:
In addition to the built-in functions and functions in the built-in modules, you can also create your own functions. 
These functions are called user-defined functions.  '''

#Function Definition
def greet():
    print("Hello World!")
# Function call
greet()

#Default Arguments : 
#Python allows to define a function with default value assigned to one or more formal arguments.

def display(name,city='Hyd'):
    print(f" Name : {name}")
    print(f" City : {city}")   
  
display("Arun","Knl")
display("Ajay")
'''Output:
 Name : Arun
 City : Knl
 Name : Ajay
 City : Hyd  '''

#Keyword Arguments :
#Python allows to pass function arguments in the form of keywords which are also called named arguments. 
#Variables in the function definition are used as keywords.

def show(name,age):
    print("Name:", name)
    print("Age:", age)
#By positional Arguments
show("Arun",20)
#By keyword Arguments
show(age=24,name="Ajay") 

'''Output :
Name: Arun
Age: 20
Name: Ajay
Age: 24  '''

#Arbitrary Arguments (*args) :
#You may want to define a function that is able to accept arbitrary or variable number of arguments.
# Moreover, the arbitrary number of arguments might be positional or keyword arguments.

def add(*nums):
    total=0
    for i in nums:
        total=total+i
    print(f"The Total is {total}")
add(10,20,30,40,50)

# Output :The Total is 150

def n(*numbers):
    largest=numbers[0]
    for i in numbers:
        if largest < i:
            largest = i
    print(f"The Largest no is {largest}")
n(12,4,9,78,45,5)

#output:The Largest no is 78

#Arbitrary Keyword Arguments (**kwargs).
#If a variable in the argument list has two asterisks prefixed to it, the function can accept arbitrary number of keyword arguments. 
#The variable becomes a dictionary of keyword:value pairs.

def details(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
details(Name="Arun",Age=20,City="Knl")
'''Output :
Name Arun
Age 20
City Knl  '''

#Variable Scope:
''' On the basis of scope, the Python variables are classified in three categories 
Local Variables
Global Variables
Nonlocal Variables'''

#Local Variables
'''A local variable is defined within a specific function or block of code. 
 It can only be accessed by the function or block where it was defined, and it has a limited scope.'''

def add():
    a=10  # Here a & b are the two local Variables.
    b=20
    print(f"Variable a {a}")
    print(f"Variable b {b}")
    return a+b
print(add())
'''Output:
Variable a 10
Variable b 20
30   '''

#Global Variables
'''A global variable can be accessed from any part of the program, and it is defined outside any function or block of code.
It is not specific to any block or function.'''
# Global variables
A = 15
B = 5
def fun():
    #Accessing global variables
    return A * B  
print(fun())

# Output: 75

#Nonlocal Variables
'''The Python variables that are not defined in either local or global scope are called nonlocal variables.
   They are used in nested functions.'''
def fun1():
    a=5
    b=5
    def fun2():
        a=4
        b=5
        print(f"Variable a {a}")
        print(f"Variable b {b}")
        return a*b
    print(fun2())
fun1()

'''Output :
Variable a 4
Variable b 5
20    '''
