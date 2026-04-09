# Topic : Sum Of N Numbers
# Time Complexity: O(N)
# Space Complexity: O(N)
def NnumbersSum(N):
    if N == 0:
        return 0
    return N + NnumbersSum(N - 1)
print(NnumbersSum(10))

        