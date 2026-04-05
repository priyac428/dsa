# Topic : Prime Number

# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
n1 = int(input("enter the number"))
count1 = 0
for i in range(1,n1+1):
        if n1 % i == 0:
              count1 += 1
if count1 == 2:
    print(f"{n1} is a prime number")
else:
    print(f"{n1} is not a prime number")

# Optimal Approach
# Time Complexity: O(sqrt(N))
# Space Complexity : O(1)
def isPrime(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count == 2
if isPrime(2) :
    print(f"it is a prime number")
else:
    print(f"it is not a prime number")

    

        