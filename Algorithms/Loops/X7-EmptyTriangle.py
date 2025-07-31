"""
*
*  *
*    *
*      *
*        *
*          *
*            *
*              *
* * * * * * * * *
"""

s = int(input("Please enter the number: "))

def triangle(s):
    #Complete the code given below
    #Replace ..... by your own code
    for i in range(s):
        if i == 0 :
            
            print("*")
            
        elif i == s - 1:
            
            print("* " * s)
            
        else:
            print("*" + "  " * i + "*")

triangle(s= s)