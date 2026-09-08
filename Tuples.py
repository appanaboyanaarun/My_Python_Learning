'''
# Tuples.
Tuple is one of the built-in data types in Python. 
A Python tuple is a sequence of comma separated items, enclosed in parentheses (). 
The items in a Python tuple need not be of same data type.
It is an ordered collection of items. Each item in the tuple has a unique position index, starting from 0.'''

# Creating Tuples 
t1=("Arun",3204,'knl',7.51)
t2=(1,2,3,4,5)
t3=("RGMCET",40,"CSEDS",'D')
t4=10,20,30,40
print(t1)
print(type(t1))
print(t2)
print(t3)
print(t4)
print(type(t4))
''' Output:
('Arun', 3204, 'knl', 7.51)
<class 'tuple'>
(1, 2, 3, 4, 5)
('RGMCET', 40, 'CSEDS', 'D')
(10, 20, 30, 40)
<class 'tuple'>  '''

# Accessing Values in Tuples.
# To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available at that index.

print("Tuple1",t1[0])
print("Tuple2",t2[1:len(t2)])
print("Tuple3",t3[-2])

'''Output:
Tuple1 Arun
Tuple2 (2, 3, 4, 5)
Tuple3 CSEDS   '''

# Updating Tuples.

#Tuples are immutable which means you cannot update or change the values of tuple elements. 
#You are able to take portions of existing tuples to create new tuples.
#t1[0]=25
#print(t1)  #Output: TypeError: 'tuple' object does not support item assignment.

tuple4= t1 + t2
print(tuple4) #Output: ('Arun', 3204, 'knl', 7.51, 1, 2, 3, 4, 5)

#Unpack Tuple Items
#The term "unpacking" refers to the process of parsing tuple items in individual variables. 
#In Python, the parentheses are the default delimiters for a literal representation of sequence object.

tuple1=(10,20,30,40)
x,y,*z=tuple1
print(tuple1)
print(x)
print(y)
print(z)

'''output:
(10, 20, 30, 40)
10
20
[30, 40]   '''


# Python Tuple Methods
'''The tuple class provides few methods to analyze the data or elements. 
These methods allows users to retrieve information about the occurrences of specific items within a tuple and their respective indices. 
Since it is immutable, this class doesn't define methods for adding or removing items. 
It defines only two methods and these methods provide a convenient way to analyze tuple data.'''

# tuple.count(obj) "Returns count of how many times obj occurs in tuple."
print(t2.count(2))
# Output: 1

# tuple.index(obj)  "Returns the lowest index in tuple that obj appears."
print(t3.index('RGMCET'))
# output:0

#NamedTuples.
'''NamedTuple is a tuple-like data structure that allows us to access tuple values using meaningful field names as well as indexes. Like tuples, NamedTuples are immutable.
Key point: NamedTuple is useful when you want the fixed/immutable nature of a tuple + readable field names.'''

from collections import namedtuple
Students=namedtuple("Students",["Name","Age","City"])
Student_Details=Students("Arun",20,"KNL")
print(Student_Details)
print(Student_Details.Name)
print(Student_Details.City)
'''Output:
Students(Name='Arun', Age=20, City='KNL')
Arun
KNL  '''