'''
Given an input num as a string. You need to typecast into an integer and double it. 
Input: num = "5"
Output: 10
Explanation: Typecast "5" to int and then double it 5 * 2 = 10

'''



user_input = str(input("Please enter the number: "))

def utility(num):
    #code here 
    num = int(num)
    return print(num * 2)

utility(num=user_input)
