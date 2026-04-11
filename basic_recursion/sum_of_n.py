# Topic : Sum Of N Numbers
# Time Complexity: O(N)
# Space Complexity: O(N)

def NnumbersSum(n):
    if n == 0:
        return 0
    return n + NnumbersSum(n - 1)
print(NnumbersSum(10))

        