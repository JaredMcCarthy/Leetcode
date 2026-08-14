
class Solution(object):
    def findClosest(self, x, y, z):
        persona1 = abs(x - z)
        persona2 = abs(y - z)
        persona3 = persona1 - persona2

        if persona1 < persona2:
            return 1
        elif persona2 < persona1:
            return 2
        else:
            return 0

sol = Solution()
print(sol.findClosest(2, 7, 4))
print(sol.findClosest(2, 5, 6))
print(sol.findClosest(1, 5, 3))