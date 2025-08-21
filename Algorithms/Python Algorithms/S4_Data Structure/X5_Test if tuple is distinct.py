'''
Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.

Examples:

Input:
arr = (1, 2, 3, 4, 5, 4)
Output: False
Input:
arr = (1, 2, 3, 4, 5)
Output: True
'''
arr = (1, 2, 3, 4, 5, 4)

if len(arr) == len(set(arr)):
    print("True")
else:
    print("False")
