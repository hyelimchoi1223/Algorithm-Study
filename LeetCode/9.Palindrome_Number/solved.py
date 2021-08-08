class Solution:
    def isPalindrome(self, x: int) -> bool:
        text_x = str(x)
        return text_x[:] == text_x[::-1]


sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
