class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res
        for i in range(1, numRows-1):
            sub = [1]
            arr = res[i]
            # print("Arr:", arr)
            for i in range(len(arr)-1):
                val = arr[i] + arr[i+1]
                sub.append(val)
            sub.append(1)
            res.append(sub)
            
        return res
                


                

        