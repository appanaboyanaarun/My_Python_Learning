'''Conditional Statements are used to control the flow of execution in a program based on specific conditions
The program execute the different blocks of code depending on whether a condition "Ture" or "False"
In Python,There are differnt types of statements
1.If Statement
2.If else Statement
3.If -elif else Statement
4.Nested if else Statement
'''

#1.If Statement.
# If statement is used to execute the block of code when the condition is True.
Age =20
if Age>=18:
    print("Your Eligible to Vote.")

#Output : Your Eligible to Vote.

#2.If else Statement.
# If else Statement is used to execute one block of code when the codition is True and another block when the codition is False.

Age=10
if Age<=12:
    print("Free Travel")
else:
    print("Pay ticket")

# Output :Free Travel

#3.If elif else Statement
#In this statement to check multiple conditions in a program .It executes a block of code when its condition is Ture ,After previous Conditions are False.
Marks=75
if Marks>=90:
    print("Grade A")
elif Marks>=80:
    print("Grade B")
elif Marks>=70:
    print("Grade C")
else:
    print("Fail")

# Output: Grade C

#4.Nested If else Statement.
# A Nested If else Statement is an If else statement inside another if or else block .
# It is used to check conditions within Another conditions

Age=45
Discount=True
if Age>40:
    if Discount:
        print("25 % Discount ")
    else:
        print("15% Discount ")
else:
    print("Not Eligible for Discount ")

# Output : 25 % Discount 

#Ternary Operator.
#Ternary Operator is a Short way to write an if else statement in a single line.

age=20
s="Adult" if age>=18 else "Minor"
print(s)

# Output :Adult

#Match Case Statement .
#It is used to compare a value in multiple patterns and execute the matching block of code .It is similar to the switch case in other programming Language.

Day=3

match Day:
    case 1:
        print("Mon")
    case 2:
        print("Tue")
    case 3:
        print("Wen")
    case 4:
        print("Thu")
    case 5:
        print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _:
        print("Invalid ")
