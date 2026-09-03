''' Strings in Python
In Python, a string is an immutable sequence of  characters.
Each character has a unique numeric value as per the UNICODE standard.
But, the sequence as a whole, doesn't have any numeric value even if all the characters are digits.
The sequence of characters is included within single, double or triple quotes in its literal representation. 
Hence,1234 is a number (integer) but '1234' is a string.
'''
# Creating  Strings.
# The same sequence of characters is enclosed, single or double or triple quotes.
msg1="Hello world"
msg2='Welcome'
msg3='''Python Programming Language'''
print(msg1)
print(msg2)
print(msg3)
'''Output :
Hello world
Welcome
Python Programming Language  '''

# Accessing Values in Strings :
'''Accessing a string means getting individual characters or a portion of a string.
Python provides two main ways:
Indexing → access one character
Slicing → access multiple characters'''

# Indexing
print(msg1[0]) 
print(msg2[2])
print(msg3[1]) 
print(msg1[-1]) # negative indexing
print(msg2[-2])
print(msg3[-12])
'''Output:
H
l
y  
d
m
i  '''

# Slicing : [start:End:Step]
print(msg1[0:4])
print(msg2[2:len(msg2)]) # Start from index 2 and continue until the end of the string.
print(msg3[5:len(msg3):2])  # Start at index 5, go until the end of the string, and take every 2nd character.
'''Output:
Hell
lcome
nPormigLnug   '''

# Updating Strings:
#You can "update" an existing string by re-assigning a variable to another string. 
#The new value can be related to its previous value or to a completely different string altogether.
msg1="Hello world"
print("New String:", msg1[:6] + "Python") # New String: Hello Python 

# Concatenate Strings in Python:
'''String concatenation in Python is the operation of joining two or more strings together. 
 The result of this operation will be a new string that contains the original strings.

 #Concatenation using '+' operator:
 The "+" operator is well-known as an addition operator, returning the sum of two numbers. 
 However, the "+" symbol acts as string concatenation operator in Python. 
 It works with two string operands, and results in the concatenation of the two.

 #Concatenation using '*' operator:
 Another symbol *, which we normally use for multiplication of two numbers, can also be used with string operands. 
 Here, * acts as a repetition operator in Python. One of the operands must be an integer, and the second a string. 
 The integer operand specifies the number of copies of the string operand to be concatenated.   '''

String1="Hello "
String2="Python"
String3 =String1 + String2
blank=" "
print(String3)  # Output : Hello Python

print(String1 * 5) # Output : Hello Hello Hello Hello Hello 

print(String1 + blank + String2) # Output:Hello  Python

# String formatting:
''' 
String formatting in Python is the process of building a string representation dynamically by inserting the value of numeric expressions in an already existing string. 
Python's string concatenation operator doesn't accept a non-string operand.'''

# % operator:
Str = "Python programming Language"
print("Welcome to the %s"  % Str)  # Output: Welcome to the Python programming Language.
# format method:
# The format() method works by defining placeholders within a string using curly braces "{}".
Str = "{} Python programming Language"
print(Str.format("Welcome to the")) # Output :Welcome to the Python programming Language

# Escape Character:
'''An escape character is a character followed by a backslash (\). 
It tells the Interpreter that this escape character (sequence) has a special meaning.
For instance, \n is an escape sequence that represents a newline. 
When Python encounters this sequence in a string, it understands that it needs to start a new line.  ''' 

print("Hello\nPython") 
print("Hello\tPython")
print("Hello \"Python\"")
print("Hello \'Python\'")
print("Hello\vPython")
print("\a")
'''Output:
Hello
Python
Hello   Python
Hello "Python"
Hello 'Python'
Hello
     Python    '''

# String Methods:
'''Python's built-in str class defines different methods. They help in manipulating strings. 
Since string is an immutable object, these methods return a copy of the original string, performing the respective processing on it. 
'''
# Case Conversion Methods:
#This category of built-in methods of Python's str class deal with the conversion of alphabet characters in the string object.

msg="welcome"
print(msg.capitalize())  # Capitalizes first letter of string.
print(msg.casefold()) #Converts all uppercase letters in string to lowercase.Similar to lower(), but works on UNICODE characters.
print(msg.lower()) #Converts all uppercase letters in string to lowercase.
print(msg.swapcase()) #Inverts case for all letters in string.
print(msg.upper()) #Converts lowercase letters in string to uppercase.
print(msg.title()) #That is, all words begin with uppercase and the rest are lowercase.
'''Output:
Welcome
welcome
welcome
WELCOME
WELCOME
Welcome   '''

# Alignment Methods.
# str class control the alignment of characters within the string object.
Message="welcome to Python Learning"
print(Message.center(40,'*')) #Returns a string padded with fillchar with the original string centered to a total of width columns.
print(Message.ljust(30,".")) #Returns a space-padded string with the original string left-justified to a total of width columns.
print(Message.rjust(30,'.')) #Returns a space-padded string with the original string right-justified to a total of width columns.
print(Message.expandtabs(10)) #Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.
print(Message.zfill(30)) #Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).
'''Output:
*******welcome to Python Learning*******
welcome to Python Learning....
....welcome to Python Learning
welcome to Python Learning
0000welcome to Python Learning  '''

#Split and Join Methods.
Str="*****String methods*****"
Message="welcome to Python Learning"
print(Str.lstrip('*')) #Removes all Left whitespace in string.
print(Str.rstrip('*')) #Removes all Right whitespace of string.
print(Str.strip('*')) # Performs both lstrip() and rstrip() on string
print(Message.rsplit(' ',1))# Splits the string from the end and returns a list of substrings
print(Message.split(' ',1)) #Splits string according to delimiter (space if not provided) and returns list of substrings.
print(Message.rpartition(','))#Splits the string in three string tuple at the ladt occurrence of separator
print(Message.partition(','))#Splits the string in three string tuple at the first occurrence of separator
text="1234Hello...."
print(text.removeprefix("1234")) #Returns a string after removing the prefix string
print(text.removesuffix('....')) #Returns a string after removing the suffix string

# Find and Replace Methods.
Message="welcome to Python Learning"
sub='e'
sub1="Python"
sub2="Learning"
print(Message.count(sub,0,len(Message))) #Counts how many times sub occurs in string  a substring of string if starting index beg and ending index end are given.
print(Message.find(sub1,0,len(Message))) #if sub occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
print(Message.index(sub2)) #Same as find(), but raises an exception if str not found.
print(Message.replace("to","the")) #Replaces all occurrences of old in string with new or at most max occurrences if max given.

# Translation Methods.


intab="aeiou"
outtab="12345"
trans=Message.maketrans(intab,outtab) #Returns a translation table to be used in translate function.
print(trans)
print(Message.translate(trans)) #Translates string according to translation table str(256 chars), removing those in the del string.

'''Output:
'''