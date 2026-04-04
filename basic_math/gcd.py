# Topic : GCD

# Brute Force Approach
# Time Complexity: O(min(a,b))
# Space Complexity: O(1)
def gcd(a,b):
    gcd = 1
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(f"gcd is {gcd}")
gcd(20,15)

# Better Approach
# Time Complexity: O(min(a,b))
# Space Complexity: O(1)
def gcd1(a1,b1):
    gcd1 = 1
    for i in range(min(a1,b1) , 0 ,-1):
        if a1 % i == 0 and b1 % i == 0:
            gcd1 = i
            break
    print(f"gcd is {gcd1}")
gcd1(40,20)

# Optimal Approach
# Time Complexity: O(log(min(a,b))) 
# Space Complexity: O(1)
def GCD(n1, n2):
    while n1 > 0 and  n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    if n1 == 0:
        print(n2)
    else:
        print(n1)
GCD(20,15)       
           