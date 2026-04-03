# Topic : Pyramid
# Time Complexity: O(N²) 
# Space Complexity: O(1)

n = int(input("Enter n: "))
    
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print("")

