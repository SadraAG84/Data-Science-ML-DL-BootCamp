'''
Input:
s = "Hello"
p = "llo"
Output: 
2
Explanation: llo starts from the second index in Hello.

'''



user_input = str(input("Please enter the word: "))
user_pattern = str(input("Please enter the pattern you want to find: "))

def findPattern(word,pattern):
    #Your code below
    
    index = word.find(pattern)
    if pattern in word.lower():
        return print(index)
    else:
        return -1
    
findPattern(word= user_input, pattern=user_pattern)