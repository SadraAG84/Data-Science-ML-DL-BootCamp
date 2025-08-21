'''Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.'''


user_input = str(input("Please enter the text: "))

def utility(s):
    i = len(s)
    for x in range(0,i,2):
        print(s[x], end="")
utility(s= user_input)