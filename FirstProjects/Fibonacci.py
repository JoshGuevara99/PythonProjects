#1,1,2,3,5,8,13,21
def printFib(n):

    if n == 0:
        return 0
            
    elif n == 1:
        return 1
            
    else: return printFib(n-1) + printFib(n-2)
            

print(printFib(6))