'''
Input: s = "Hello"
Output: ell
Explanation: The first and last character are ignored.

'''



user_input = str(input("Please enter the word: "))


def sliceString(word):
    #Write your code below
    return word[1:-1]

sliceString(word= user_input)