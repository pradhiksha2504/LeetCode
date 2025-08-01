class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            sub = res[-1]
            arr = [1]
            for j in range(1,len(sub)):
                val = sub[j-1] + sub[j]
                arr.append(val)
            arr.append(1)
            res.append(arr)
            
        return res
                


                

        