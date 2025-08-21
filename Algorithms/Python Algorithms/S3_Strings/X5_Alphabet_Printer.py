'''
Input:
c1 = 'a'
c2 = 'z'
Output: 
a b c d e f g h i j k l m n o p q r s t u v w x y z
Explanation:  Printed alphabets from a to z.

'''

first_letter = str(input("Please enter the first letter: "))
last_letter = str(input("Please enter the last letter: "))

#User function Template for python3
def alphabets(c1,c2):
    
    #Code below to print alphabets from c1 to c2
    # Don't provide a new line after printing
    c1_ord = ord(c1)
    c2_ord = ord(c2)
    

    
    for i in range(c1_ord, c2_ord + 1):
        print(chr(i), end=" ")

alphabets(c1=first_letter, c2=last_letter)
