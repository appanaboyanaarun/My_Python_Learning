'''Dictionaries in Python
In Python, a dictionary is a built-in data type that stores data in key-value pairs. 
A dictionary is a mutable collection of key-value pairs. 
It preserves insertion order, and its values are accessed using keys rather than numeric indexes.
A mapping object 'maps' the value of one object to another. 
To establish mapping between a key and a value, the colon (:) symbol is put between the two.
Each key-value pair is separated by a comma and enclosed within curly braces {}. 
The key and value within each pair are separated by a colon (:), forming the structure key:value.
'''
#Creating a Dictionary
'''You can create a dictionary in Python by placing a comma-separated sequence of key-value pairs within curly braces {}, with a colon : separating each key and its associated value.
Alternatively, you can use the dict() function.
Only a number, string or tuple can be used as key. 
All of them are immutable. You can use an object of any type as the value.
You can assign a value to more than one keys in a dictionary, but a key cannot appear more than once in a dictionary.'''

# Creating Dictionary using Curly Braces
Student_info ={"Name":"Arun","Age":20,"Dept":"CSEDS"}
print("Dictionary using Curly Braces:",Student_info)
#Output:  Dictionary using Curly Braces: {'Name': 'Arun', 'Age': 20, 'Dept': 'CSEDS'}

D1={"Fruits":("Mango","Banana","Apple"),"Flowers":("Rose","Jasmeen","Lotus")}
print("Assign Multiple values to the one Key:",D1)
#Output:Assign Multiple values to the one Key: {'Fruits': ('Mango', 'Banana', 'Apple'), 'Flowers': ('Rose', 'Jasmeen', 'Lotus')}

#Creating Dictionary Using dict() function
Di=dict(Name="Ajay",Age=20,Dept="CSE")
print("Dictionary using dict():",Di)
#Output:Dictionary using dict(): {'Name': 'Ajay', 'Age': 20, 'Dept': 'CSE'}

#Accessing Dictionary Items
#You can access the value associated with a specific key using square brackets [] or the get() method.
Name=Student_info["Name"]
print("Name:",Name)      # Output: Name: Arun
Age=Student_info.get("Age")
print("Age:",Age)       #Output: Age: 20

#Modifying Dictionary Items
#You can modify the value associated with a specific key or add a new key-value pair
Student_info["Age"]=19
print("Modifying Age:",Student_info)   #Output:  Modifying Age: {'Name': 'Arun', 'Age': 19, 'Dept': 'CSEDS'}
#Adding Dict item
Student_info["Graduation_Year"]=2028
print("Modified Dict is ",Student_info) #Output: Modified Dict is  {'Name': 'Arun', 'Age': 19, 'Dept': 'CSEDS', 'Graduation_Year': 2028}

#Removing Dictionary Items
#You can remove items using the del statement, the pop() method, or the popitem() method.
# Removing an item from Dict using del statement
del Student_info["Age"]
print("After removing item ",Student_info)
#Output: After removing item  {'Name': 'Arun', 'Dept': 'CSEDS', 'Graduation_Year': 2028}

Graduation=Student_info.pop("Graduation_Year")
print(Student_info)     # Output:{'Name': 'Arun', 'Dept': 'CSEDS'}

Student_info.popitem()
print(Student_info)  # Output: {'Name': 'Arun'}

# Remove Dictionary Items Using a Loop
Student_info1 ={"Name":"Arun","Age":20,"Dept":"CSEDS"}
keys_to_remove=["Age","Dept"]
for key in keys_to_remove:
    Student_info1.pop(key,None)
print(Student_info1)

#Dictionary Veiw obj by loops.
'''The items(), keys(), and values() methods of dict class return view objects. 
These views are refreshed dynamically whenever any change occurs in the contents of their source dictionary object.
#The items() Method
The items() method returns a dict_items view object. It contains a list of tuples, each tuple made up of respective key, value pairs.'''

for keys,values in Di.items():
    print(f"{keys} {values}")

'''output:
Name Ajay
Age 20
Dept CSE    '''

#The keys() Method
#The keys() method of dict class returns dict_keys object which is a list of all keys defined in the dictionary. 
for keys in D1.keys():
    print(keys)

# Output:Fruits
#        Flowers

#The values() Method
#The values() method returns a view of all the values present in the dictionary. The object is of dict_value type, which gets automatically updated.
for values in D1.values():
    print(values)

'''Output:
('Mango', 'Banana', 'Apple')
('Rose', 'Jasmeen', 'Lotus')   '''

#Copy Dictionaries
#Copying dictionaries in Python refers to creating a new dictionary that contains the same key-value pairs as the original dictionary.

Original_dict={
    "Name":"Arun",
    "Age":20,
    "Dept":"CSD",
    "College":"RGM"
}
print("The original_Dict:",Original_dict) 
# Output: The original_Dict: {'Name': 'Arun', 'Age': 20, 'Dept': 'CSD', 'College': 'RGM'}

Copy_dict=Original_dict.copy()
print("Copy From Original Dict",Copy_dict)  
# Output: Copy From Original Dict {'Name': 'Arun', 'Age': 20, 'Dept': 'CSD', 'College': 'RGM'}

Copy_method2=dict(Original_dict)
print("Another method for Copy Original_dict",Copy_method2)  
#Output: Another method for Copy Original_dict {'Name': 'Arun', 'Age': 20, 'Dept': 'CSD', 'College': 'RGM'}

import copy
deep_copy=copy.deepcopy(Original_dict)
print(deep_copy)
# Output: {'Name': 'Arun', 'Age': 20, 'Dept': 'CSD', 'College': 'RGM'}

#Nested Dictionaries:

nested_dict={"Student1":
             {"Name":"Arun","Age":20},
             "Student2":
             {"Name":"Ajay","Age":19}
}
nested_dict["Student3"]={"Name":"Venu","Age":21}
for keys,values in nested_dict.items():
    print(f"{keys} {values}")

'''Output:
Student1 {'Name': 'Arun', 'Age': 20}
Student2 {'Name': 'Ajay', 'Age': 19}
Student3 {'Name': 'Venu', 'Age': 21}  '''