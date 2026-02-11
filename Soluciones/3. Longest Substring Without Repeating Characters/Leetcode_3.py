

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ventana = set()
        max_longitud = 0
        inicio = 0

        for fin in range(len(s)):
            while s[fin] in ventana:
                ventana.remove(s[inicio])
                inicio += 1
            
            ventana.add(s[fin])
            max_longitud = max(max_longitud, fin - inicio + 1)
        
        return max_longitud


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))