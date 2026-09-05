
# Python Lists
'''
A list is one of the built-in data types in Python.
A Python list is an ordered collection of items enclosed
in square brackets [ ].
Example:
    [1, 2, 3, 4, 5]
List items:
- Can be of different data types
- Have a unique index starting from 0
- Can be modified because lists are mutable
- Can contain duplicate values
'''
# 1. Creating Lists.
List1=[1,5,9,7,5,3]
List2=['Python','Java',3204,202]
print(List1)
print(List2)

'''Output:
[1, 5, 9, 7, 5, 3]
['Python', 'Java', 3204, 202]    '''

# Accessing Values in Lists.
#To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index.
print(List1[2])  # Output: 9
print(List2[1:len(List2)])  # Output: ['Java', 3204, 202]
print(List2[-2]) # Output: 9

#Updating Lists.
#You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator.
#And you can add to elements in a list with the append() method.
List2.append("Data Science") #The append() method in Python is used to add a single element to the end of a list.
print(List2)
List1.extend(List2) #The extend() method in Python is used to add multiple elements from an iterable (such as another list) to the end of a list.
print(List1)
List1.insert(0,"Welcome") #The insert() method in Python is used to add an element at a specified index (position) 
print(List1)
'''Output :
['Python', 'Java', 3204, 202, 'Data Science']
[1, 5, 9, 7, 5, 3, 'Python', 'Java', 3204, 202, 'Data Science']
['Welcome', 1, 5, 9, 7, 5, 3, 'Python', 'Java', 3204, 202, 'Data Science']    '''

#Removing List Items.
'''Removing list items in Python implies deleting elements from an existing list.
Lists are ordered collections of items, and sometimes you need to remove certain elements from them based on specific criteria or indices. 
We can remove list items in Python using various methods such as remove(), pop() and clear().
Additionally, we can use the del statement to remove items at a specific index. '''

List1.remove('Welcome')  #the remove() method by specifying the value we want to remove within the parentheses
print(List1)
List1.pop(2) #The pop() method in Python is used to removes and returns the last element from a list if no index is specified, or removes and returns the element at a specified index
print(List1)
List1.clear() #The clear() method in Python is used to remove all elements from a list, leaving it empty.
print(List1)
'''Output:
[1, 5, 9, 7, 5, 3, 'Python', 'Java', 3204, 202, 'Data Science']
[1, 5, 7, 5, 3, 'Python', 'Java', 3204, 202, 'Data Science']
[]    '''

# Loop Through List Items.
'''Looping through list items in Python refers to iterating over each element within a list. 
We do so to perform the desired operations on each item.
These operations include list modification, conditional operations, string manipulation, data analysis, etc'''

for i in List2:
    print(i,end=" ")

# Output : Python Java 3204 202 Data Science 

index=0
while index < len(List2):
    print(List2[index])
    index +=1

'''Output:
Python
Java
3204
202
Data Science   '''

#Iterate using List Comprehension.
'''A list comprehension in Python is a concise way to create lists by applying an expression to each element of an iterable. 
These expressions can be arithmetic operations, function calls, conditional expressions etc.'''
number=[1,2,3,4,5]
SquareNumbers=[nums**2 for nums in number ]
print(SquareNumbers)

#Output: [1, 4, 9, 16, 25]
#Iterate using the enumerate() Function.
#The enumerate() function in Python is used to iterate over an iterable object while also providing the index of each element.
for index,SquareNumbers in enumerate(SquareNumbers):
    print(index,SquareNumbers)
'''Output:
0 1
1 4
2 9
3 16
4 25    '''

# List Comprehension in Python.
'''A list comprehension is a concise way to create lists. It is similar to set builder notation in mathematics. 
It is used to define a list based on an existing iterable object, 
such as a list, tuple, or string, and apply an expression to each element in the iterable.'''

Str="Python programming language"
Double_Str=[Char.upper() for Char in Str  if Char not in "aeiou"]
print(Double_Str)
# Output:['P', 'Y', 'T', 'H', 'N', ' ', 'P', 'R', 'G', 'R', 'M', 'M', 'N', 'G', ' ', 'L', 'N', 'G', 'G']

lis=[x for x in range(1,11) if x%2==0]
print(lis)
# Output. [2, 4, 6, 8, 10]

Double_num=[(lambda x:x**2)(x) for x in number]
print(Double_num)
# Output:[1, 4, 9, 16, 25]

# Sort.
'''
The python sort() method is used to sort the elements of a list in place. This means that it modifies the original list and does not return a new list.
#Syntax.
list_name.sort(key=None, reverse=False)
'''
S=['ML','OS','SE','IQTA','EN&VC']
print("Original List",S)
S.sort()
print("After Sorting",S)
S1=sorted(S,reverse=True)
print(S1)
'''Output:
Original List ['ML', 'OS', 'SE', 'IQTA', 'EN&VC']
After Sorting ['EN&VC', 'IQTA', 'ML', 'OS', 'SE']
['SE', 'OS', 'ML', 'IQTA', 'EN&VC']'''

def MyFunction(x):
    return x%10
li=[10,75,12,35,23,5]
li.sort(key=MyFunction)
print(li) 

#OUtput:[10, 12, 23, 75, 35, 5]
