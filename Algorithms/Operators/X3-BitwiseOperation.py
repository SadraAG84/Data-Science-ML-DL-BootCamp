"""
Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~ e
Note: ^ is for xor.

Examples:

Input: a = 1, b = 2, c = 3
Output: 0 -2 0 3
Explanation: We print d e f g after performing the given operations.

"""

def operators(a, b, c):
    #Do a^a below
    d= a ^ a
    #Do c^b below
    e= c ^ b
    #Do a&b below
    f= a & b
    #Do c|(a^a) below
    g= c | (a^a)
    #Do ~e below
    e= ~e

    #The line below prints the output. Don't change it!
    print(d,e,f,g)