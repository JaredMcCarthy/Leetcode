
class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))

