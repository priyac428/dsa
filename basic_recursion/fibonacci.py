# Topic : Fibonacci

# Recursive Approach
# Time Complexity: O(2^N) 
# Space Complexity: O(N) 
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(3))
        

# iterative Approach
# Time Complexity: O(N) 
# Space Complexity: O(1) 
def fib1(n1):
    if n1 <= 1:
        return n1
    slast1 = 0
    last1 = 1
    for i in range(2 , n1+1):
        cur1 = slast1 + last1
        slast1 = last1
        last1 = cur1
        return cur1 
print(fib1(5))

         
        