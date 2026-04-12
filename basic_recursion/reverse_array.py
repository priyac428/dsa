# Topic : Reverse an Array

# Better Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
arr = [1,2,3,4,5]  
n = 5 
p1 = 0
p2 = n - p1 - 1
while p1 < p2: 
    arr[p1],arr[p2] = arr[p2],arr[p1]
    p1 += 1
    p2 -= 1
print(arr)
