class Solution:
    def romanToInt(self, s: str) -> int:
        basic = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        count = basic[s[0]]
        temp = count
        for i in range(1,len(s)):
            val = basic[s[i]]
            if val <= temp:
                count += val
            else:
                val = abs(temp - val)
                count = (count - temp) + val
            temp = val
        return count
        