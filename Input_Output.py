'''
What is Input?
Input is the data given by the user to a program.
Python uses the input() function to receive input.'''

name = input("Enter your name: ")
print(name)

# Important: input() always returns a string.

#2.Taking Different Data Types
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

#3.Multiple Inputs in One Line
#Python provides split() to separate multiple values entered on the same line.

first_name, last_name = input("Enter first and last name: ").split()
full_name = last_name + " " + first_name
print(full_name)

#4.Multiple Integer Inputs
#Use map(int, ...) when all values should be integers.

age, marks, reg_no = map(int,input("Enter age, marks and registration number: ").split())

print(f"Your age is {age}.")
print(f"You got {marks} marks.")
print(f"Your registration number is {reg_no}.")

#5.Taking Multiple Values as a List
#This is very important for programming problems

marks = list(map(int, input("Enter the marks: ").split()))
print(marks)

'''Output
The print() function displays information.'''

name = "Arun"
age = 20
print(name)
print(age)

#2.Formatted Output
#For professional Python code, learn f-strings.
name = "Arun"
age = 20
marks = 85.5
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks}")

'''INPUT

├── input()                  → String
├── int(input())             → Integer
├── float(input())           → Float
├── input().split()          → Multiple values
├── map(int, ...)            → Convert to integers
├── map(float, ...)          → Convert to floats
└── list(map(int, ...))      → List of integers

OUTPUT

├── print()                  → Display output
├── f"..."                   → Formatted output
├── sep="..."                → Change separator
└── end="..."                → Control line ending

'''