class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num = len(candyType) // 2
        f = {}

        for i in candyType:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        
        types = f.keys()
        if len(types) >= num:
            return num
        return len(types)

        