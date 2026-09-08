'''Sets in Python.
In Python, a set is an unordered collection of unique elements. 
Unlike lists or tuples, sets do not allow duplicate values i.e. each element in a set must be unique. 
Sets are mutable, meaning you can add or remove items after a set has been created.
Sets are defined using curly braces {} or the built-in set() function.'''

#Creating a Set in Python
#Creating a set in Python refers to defining and initializing a collection of unique elements. 
#You can create a set in Python using curly braces {} or the set() function.Du
my_set={1,2,3,4,5}
print(my_set) #Output: {1, 2, 3, 4, 5}

# Using Set() function.
# you can create a set using the set() function by passing an iterable (like a list or a tuple) containing the elements you want to include in the set.
my_set1=set([10,20,30,40,50])
print(my_set1) #Output:{40, 10, 50, 20, 30}

#Duplicate Elements in Set
# Sets in Python are unordered collections of unique elements. 
# If you try to create a set with duplicate elements, duplicates will be automatically removed 

dup_set={1,4,5,8,3,7,6,1,4,5,}
print(dup_set)  #Output:{1, 3, 4, 5, 6, 7, 8}

#Access Set Items.
#In Python, sets are unordered collections of unique elements, and unlike sequences (such as lists or tuples), sets do not have a positional index for their elements. 
#This means that you cannot access individual elements of a set directly by specifying an index.

Access_setItems={items+100 for items in my_set1 }
print(Access_setItems)  # Output: {130, 140, 110, 150, 120}

for i in my_set1:
    print(i)
'''Output:
40
10
50
20
30   '''

# Add Set Items.
'''Adding set items implies including new elements into an existing set. 
In Python, sets are mutable, which means you can modify them after they have been created. 
While the elements within a set must be immutable (such as integers, strings, or tuples), the set itself can be modified.
You can add items to a set using various methods, such as add(), update(), or set operations like union (|) and set comprehension'''

# The add() method in Python is used to add a single element to the set.
my_set.add(10)
print(my_set)  # Output:{1, 2, 3, 4, 5, 10}

#In Python, the update() method of set class is used to add multiple elements to the set. 
my_set.update([20,30,40,50])
print(my_set)  #Output: {1, 2, 3, 4, 5, 10, 20, 30, 40, 50}

'''Remove Set Items
Removing set items implies deleting elements from a set. 
In Python, sets are mutable, unordered collections of unique elements, and there are several methods available to remove items. 
We can remove set items in Python using various methods such as remove(), discard(), pop(), clear(), and set comprehension'''

#The remove() method in Python is used to remove the first occurrence of a specified item from a set.
my_set.remove(20)
print(my_set)  # Output:{1, 2, 3, 4, 5, 10, 30, 40, 50}

#The discard() method in set class is similar to remove() method. 
#The only difference is, it doesn't raise error even if the object to be removed is not already present in the set collection.
my_set.discard(30)
my_set.discard(30)
print(my_set)  #Output:{1, 2, 3, 4, 5, 10, 40, 50}

#The clear() method in set class removes all the items in a set object, leaving an empty set.
my_set.clear()
print(my_set)  #Output: set()

'''Set Operators in Python
The set operators in Python are special symbols and functions that allow you to perform various operations on sets, such as union, intersection, difference, and symmetric difference. 
These operators provide a way to combine, compare, and modify sets.'''

#UNION 
#The union of two sets is a set containing all distinct elements that are in A or in B or both.
#This operation combines the elements of two sets while eliminating duplicates, resulting in a new set containing all unique elements from both sets

set1={1,2,3}
set2={3,4,2,5}
set3=set1 | set2  # Another way set3=set1.union(set2)
print(set3)   # Output: {1, 2, 3, 4, 5}

#Intersection .
#The intersection of two sets AA and BB, denoted by A∩B, consists of all elements that are common to both in A and B.
# Python provides the intersection() function or the & operator to perform this operation.

set4=set1 & set2
print(set4)    # Output: {2, 3}

#Difference 
# The difference (subtraction) between two sets consists of elements present in the first set but not in the second set. 
# It is defined as follows.  The set AB consists of elements that are in A but not in B.

set5 = set1 -set2
print(set5)     # OUtput: {1}

# Symmetric Difference 
#The symmetric difference of two sets consists of elements that are present in either set but not in both sets.

set6  = set1 ^ set2
print(set6)   #Output:{1, 4, 5}