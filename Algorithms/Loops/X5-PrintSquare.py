"""Input: s = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square! Each side contains s = 4 *."""

s = int(input("Please enter the number: "))

def printSquare(s):
        for i in range(s):
            if i == 0 or i == s - 1: 
                print("* " * s)
            else:
                print("*" + " " * (2 * s - 3) + "*")

printSquare(s= s)