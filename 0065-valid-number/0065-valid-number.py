class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Remove any leading or trailing whitespaces
        
        try:
            num = float(s)  # Try converting the string to a float
            if "inf" in s.lower() or num != num :
                return False
            return True
        except ValueError:
            return False
