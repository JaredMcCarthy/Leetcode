
class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()
        if word:
            lastword = word[-1]
            return len(lastword)
        else:
            return 0

sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))