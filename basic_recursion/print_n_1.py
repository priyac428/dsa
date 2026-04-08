# Topic : Print Numbers From N To 1

# Time Complexity: O(N)
# Space Complexity: O(N)
def printNumbers(n):        
    if n == 0:
        return
    print(n,end="")
    print("")
    printNumbers(n-1)    
printNumbers(5) 

        