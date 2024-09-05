class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        miss = (mean*(len(rolls)+n)) - sum(rolls)
        if miss < n or miss > n*6:
            return []
        res = [1]*n
        miss -= n
        for i in range(n):
            x = min(5, miss)
            res[i] += x
            miss -= x

            if miss <= 0:
                break
            
        return res
        