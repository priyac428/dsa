# Topic : Basic square
# Time Complexity: O(N²) 
# Space Complexity: O(1)

n = int(input("Enter n: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print("")