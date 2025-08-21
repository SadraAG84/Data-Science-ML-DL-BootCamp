'''
Given two sets a and b. check whether a is subset of b ?

a is subset of b, if all elements of a set a are present in another set b.

Examples:

Input: a = [1, 4, 3], b = [1, 4, 3, 2]
Output: True
'''

list1 = []
list2 = []

def getting_elements1():
    num_elements = int(input("How many elements do the list1 will have? "))
    for i in range(num_elements):
        value = int(input(f"Please enter the value of {i + 1}.element: "))
        list1.append(value)

def getting_elements2():
    num_elements = int(input("How many elements do the list2 will have? "))
    for i in range(num_elements):
        value = int(input(f"Please enter the value of {i + 1}.element: "))
        list2.append(value)


def checkSubset(list1, list2):
    for item in list1:
        if item not in list2:
            return print("False")
    return print("True")
    
getting_elements1()
getting_elements2()
checkSubset(list1=list1, list2=list2)