'''
Given two sets A and B. find the Union of both the sets.

Union of two given sets A and B is a set which consists of all the elements of A 
and all the elements of B such that no element is repeated.

Input:
A = {2, 5, 6}
B = {1, 4, 3, 2}
Output: 
1 2 3 4 5 6

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
        list1.append(value)



def Union(list1, list2):
        
    union = list(set(list1) | set(list2))
    return print(f"the Union of two list is: {union}")

getting_elements1()
getting_elements2()
Union(list1=list1, list2=list2)