'''
Input:
s = "Hello"
Output: 
False
Explanation: Hello is not equal to olleH
so it's not a palindrome.

'''



user_input = str(input("Please enter the word: "))

def isPalin(word):
    #Your code below
    #Remeber to ignore the case when comparing
    reversed_word = ''.join(reversed(word))
    
    if word.lower() == reversed_word.lower():
        return True
    else:
        return False
    
isPalin(word=user_input)