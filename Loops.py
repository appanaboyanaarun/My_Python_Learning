'''Python loops allow us to execute a statement or group of statements multiple times.
In general, statements are executed sequentially.There may be a situation when you need to execute a block of code several number of times.
Types of Loops
1.for loop.
2.while loop.
3.Nested loop.

'''
#For Loop
'''The for loop in Python provides the ability to loop over the items of any sequence.
It performs the same action on each item of the sequence. This loop starts with the for keyword, 
followed by a variable that represents the current item in the sequence.
The in keyword links the variable to the sequence you want to iterate over. 
A colon (:) is used at the end of the loop .
Python's built-in range() function returns an iterator object that streams a sequence of numbers.
This object contains integers from start to stop, separated by step parameter.
You can run a for loop with range as well.    '''
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# Output : 120

#While loop 
'''A while loop in Python repeatedly executes a target statement as long as the specified expression is True 
This loop starts with while keyword followed by a boolean expression and colon symbol (:).
Then, an indented block of statements starts.'''

name =input("Enter Username:")
while name=="":
    name =input(" Please Enter Username:")
print(f" Hello Welcome {name}")

'''Output : Enter Username:
 Please Enter Username:
 Please Enter Username:
 Please Enter Username:Arun
 Hello Welcome Arun   '''
#3.Nested loop.
'''In Python, when you write one or more loops within a loop statement that is known as a nested loop. 
The main loop is considered as outer loop and  inside the  loop are known as inner loops.'''

n=5
for i in range(1,n+1):   # outer loop - no of rows 
    for j in range(i):   # inner loop - no of columns 
        print("*",end="")
    print()

'''  Output:
*
**
***
****
*****  '''
# break statement
'''Python break statement is used to terminate the current loop and resumes execution at the next statement, 
just like the traditional break statement in C.
break statement is when some external condition is triggered requiring a sudden exit from a loop. 
The break statement can be used in both Python while and for loops.
'''
for i in range (1,6):
    if i ==3:
        break
    print(i)
print(f" The For loop is exit at  {i}")

'''Output :
1
2
The For loop is exit at  3 '''

#Continue Statement.
'''Continue statement is used to skip the execution of the program block and returns the control to the beginning of the current loop to start the next iteration.
   If the condition becomes TRUE, the continue statement will skip the current iteration and proceed with the next iteration of the loop.   '''

for i in range(1,6):
    if i == 4:
        continue
    print(i)
print(f"Skips when i == 4  and execute next step")

''' Output :
1
2
3
5
Skips when i ==4  and execute next step   '''

# Pass Statement 
'''Python pass statement is used when a statement is required syntactically but you do not want any command or code to execute. 
It is a null which means nothing happens when it executes. 
This is also useful in places where piece of code will be added later, 
but a placeholder is required to ensure the program runs without errors.'''

for i in range (1,6):
    if i==3:
        pass
    print(i)

'''Output:
1
2
3
4
5

'''