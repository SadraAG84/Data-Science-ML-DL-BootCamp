'''
Input:s = "Hello"
Output:olleH
Explanation: Reverse of Hello is olleH

'''



user_input = str(input("Please enter the word: "))

def reverser(word):
    reversed_word = ''.join(reversed(word))
    return print(reversed_word)

reverser(word= user_input)