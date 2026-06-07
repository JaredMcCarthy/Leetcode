
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
                    
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = 0
        return [1] + [0] * len(digits)

sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([4,3,2,1]))
print(sol.plusOne([9]))