# Topic : Print Numbers From 1 To N

# Time Complexity: O(N)
# Space Complexity: O(N)
def printNumbers(n):        
    if n == 0:
        return
    printNumbers(n-1)
    print(n,end="")
    print("")
printNumbers(5) 

        