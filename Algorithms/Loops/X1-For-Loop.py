'''Input:
n = 5
Output:
5 10 15 20 25 30 35 40 45 50'''

#User function Template for python3


def utility():
    n = int(input("Enter the number: "))
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11):  ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * n, end=" ")  ## Separating by spaces using end =" "
utility()