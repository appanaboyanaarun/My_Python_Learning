# Increasing Triangle.

for i in range (1,6):
    for j in range(i):
        print("*",end="")
    print()

'''Output:
*
**
***
****
*****   

'''

#Decreasing Triangle.
for i in range(6,0,-1):
    print("*" * i)

'''Output:
*****
****
***
**
*

'''

#Right-Aligned Triangle.

for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

'''Output:
     *
    **
   ***
  ****
 *****   '''

#Pyramid Pattern

for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for k in range( 2 * i -1):
        print("*",end="")
    print()

'''Output :

     *
    ***
   *****
  *******
 *********

'''
# Inverted Pyramid Pattern

for i in range(5,0,-1):

    for j in range(6-i):
        print(" ",end="")

    for k in range( 2 * i -1):
        print("*",end="")
    print()

'''Output:

 *********
  *******
   *****
    ***
     * 
'''

# Diamond Pattern

for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for k in range(2 * i -1):
        print("*",end="")
    print()

for m in range(6-1,0,-1):
    for j in range(6-m):
        print(" ",end="")
    for o in range(2 * m -1):
        print("*", end="")
    print()

'''Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''



