"""
Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True. First a is checked then b is checked. a or b checks if either of a or b is True. If one is True; it doesn't check for the other. not a complements the boolean value of a.
Note: 0 and empty string are False and all other values are True.
In this question you basically need to do
a and b
a or b
not a

Examples:

Input: a = 0, b = 2
Output: 0 2 True
Explanation: 0 and 2 gives 0. 0 or 2 gives 2. not 0 give True as 0 is False.

"""

def utility():
    #The two lines below take input. Don't change them!
    a=int(input())
    b=int(input())
    
    #Do a and b below
    p = a and b
    #Do a or b below
    q = a or b
    #Do not a below
    r = not a

    #The code below prints the output. Don't change it!
    print(p,q,r)