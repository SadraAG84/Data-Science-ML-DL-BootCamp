'''Input: x = 3
Output: 3 2 1 0
Explanation: Numbers in decreasing order from 3 are 3 2 1 0.'''



user_input = int(input("Please enter the number: "))
def utility(x):
    while(x >= 0):
        print(x, end=" ")
        x -= 1

utility(x= user_input)