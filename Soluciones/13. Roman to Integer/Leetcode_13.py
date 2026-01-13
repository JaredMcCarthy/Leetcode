
class Solution(object):
    def romanToInt(self, s):
        roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_value = 0
        int_value = 0
        for i in range(len(s) - 1, -1, -1):
            valor = roman_val[s[i]]
            if valor < prev_value:
                int_value -= valor
            else:
                int_value += valor
            prev_value = valor
        return int_value
    
sol = Solution()
print(sol.romanToInt("XVX"))