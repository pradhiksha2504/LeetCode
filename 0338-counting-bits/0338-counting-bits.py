class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1, 1]
        if n <= 2:
            return res[:n+1]
        for i in range(3, n+1):
            x = bin(i).replace("0b","")
            res.append(x.count("1"))
        return res
        


        
        
        