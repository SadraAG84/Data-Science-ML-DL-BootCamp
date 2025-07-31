"""
Input: S = 4
Output:
* * * * 
* * * 
* * 
*
"""

s = int(input("Please enter the number: "))

def invTriangleWall(s):
    #Complete the given code
    for i in range(s, 0, -1):
        print("* " * i)

invTriangleWall(s= s)