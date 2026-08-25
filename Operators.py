'''Operations are Symbols that perfroms operations on variables and values  
   An opertor is a Symbol that tells the computer to perfrom on opearation on one or more values(operands)
   Ex:
   10+20 # 10&20 are the two operands
   '+' is the operator
   Output :30 
Types of Operators 
1.Arithmetic Operators
2.Assignment Operators
3.Relational (Comparison )Operators 
4.Logical Operators
5.Unary operators
6.Bitwise Operators
7.Ternary (Conditional) Operators
'''

# Arithmetic Operators
#used to perform mathematical Calculations.
a=20;
b=10;
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
'''Output :
30
10
200
2.0
0'''

# Assignment Operators 
# Used to assign values to  Variables
a,b,c,d=10,15,5,9
a+=16;
b-=2;
c*=5;
d/=3;
print(a)
print(b)
print(c)
print(d)
'''Output:
26
13
25
3.0 '''

#Relational (Comparison )Operators
#Used to compare two values
a=10;
b=10;
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a>=b)
'''Output :
True
False
False
False
True
True'''

#Logical Operators
#Used with boolean values
a=10;
b=5;
print(a and b)
print(a or b)
print(not a)
'''
Output:
5
10
False'''

#Unary operators
#Operate on a Single Operand
# Python does not have ++ and -- operators Instead Use
a=5
a+=10
print(a) 
# Output:15

#Bitwise Operators
#Operate on Binary Values
a=10
b=3
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a>>b)
print(a<<b)

'''
Output:
2
11
9
-4
1
80
'''



