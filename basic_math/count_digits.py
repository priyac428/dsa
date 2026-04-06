# Topic : Count Digits

# Brute Force Approach
# Time Complexity:O(log10(N) + 1),
# Space Complexity: O(1)
import math  # this is for optimal approach
n = int(input("enter the value of n: "))
if n == 0:
    print("1")
else:
    count = 0
    while n > 0:
        count += 1
        n =  n // 10
    print(count)

# Optimal Approach
# Time Complexity: O(1) 
# Space Complexity: O(1)
n1 = int(input("enter the value of n1: ")) 
if n1 == 0:
    print("1")
else:
    count1 = int(math.log10(n1)+1)
    print(count1)

