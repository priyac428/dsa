# Topic : Palindrome

# Time Complexity: O(log10(N)) 
# Space Complexity: O(1)
n = int(input("enter the value of n: "))
reverse = 0
dup = n
while n > 0:
    last_digit = n % 10
    reverse = reverse * 10 + last_digit
    n =  n // 10
if dup == reverse :
    print("palindrome")
else :
    print(" not palindrome")
        
