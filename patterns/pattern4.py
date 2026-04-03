# Topic :  Inverted Right Angled Triangle 
# Time Complexity: O(N²) 
# Space Complexity: O(1)

n = int(input("enter the value of n: ")) 
for i in range(n):
    for j in range(n,i,-1):
        print("*",end="")
    print("")