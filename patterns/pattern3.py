# Topic : Right Angled Triangle With Numbers
# Time Complexity: O(N²) 
# Space Complexity: O(1)

n = int(input("enter the value of n: ")) 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
            