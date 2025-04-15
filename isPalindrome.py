class Solution:
    def isPalindrome(self, x: int) -> bool:
# x1 = 1 2 1
# x2 = 1 2 1
return str(x) == str(x)[::-1]

if __name_ == 'main':
    s = Solution()
    x = 121

    result = s.isPalindrome(x)
    print("Result: {result}")
