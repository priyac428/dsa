 # Topic : Palindrome

# Time Complexity: O(N)
# Space Complexity: O(1) 
def palindromeCheck(s):
    left = 0
    right = len(s) - 1
        
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True
print(palindromeCheck("madam"))