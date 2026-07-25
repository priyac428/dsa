# Topic : Armstrong Numbers
# Optimal Approach
# Time Complexity: O(log10N + 1) 
# Space Complexity: O(1)

def isArmstrong(n):
    dup = n
    k = len(str(n))
    sum = 0
    while n > 0:
        last_digit = n %10
        sum = sum + last_digit ** k
        n = n // 10
    return dup == sum
print(isArmstrong(153))
print(isArmstrong(1543))
