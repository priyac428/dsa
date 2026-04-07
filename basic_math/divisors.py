# Topic : Divisors

# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
def divisors(n):
    list1 = []
    for i in range(1,n+1):
        if n % i == 0:
            list1.append(i)
    return list1
print(divisors(10))

# Optimal Approach
# Time Complexity: O(sqrt(N))
# Space Complexity: O(sqrt(N))   
def divisors1(n1):
    list2 = []
    for i in range(1,int(n1**0.5)+1):
        if n1 % i == 0:
            list2.append(i)
            if n1//i != i:
                list2.append(n1//i)
    list2.sort()
    return list2
print(divisors1(20)) 

