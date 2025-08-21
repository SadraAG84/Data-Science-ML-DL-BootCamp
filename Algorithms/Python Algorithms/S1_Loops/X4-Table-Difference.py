'''  Input: n1 = 9, n2 = 4
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  9 18 27 36 45 54 63 72 81 90
- 4  8 12 16 20 24 28 32 36 40
-----------------------------------------
= 5 10 15 20 25 30 35 40 45 50 '''

n1 = 9
n2 = 4

def difference(n1,n2):
    
    x = 1
    n1Numbers = []
    n2Numbers = []
    
    print(" ", end="")
    while(x <= 10):
  
        number = n1 * x
        print(number, end=" ")
        n1Numbers.append(number)
        x += 1
    print("")
    print("-", end="")
    x = 1
    while(x <= 10):

        number = n2 * x
        print(number, end=" ")
        n2Numbers.append(number)
        x += 1
    print("")
    print("------------------------------")
    
    for x in range(len(n1Numbers)):
        
        diffNumber = n1Numbers[x] - n2Numbers[x]
        print(diffNumber, end=" ")
    
difference(n1= n1, n2= n2)