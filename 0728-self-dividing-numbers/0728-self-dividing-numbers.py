class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            flag = 0
            # print(i)
            for j in str(i):
                # print(j)
                if j=='0' or i%int(j)!=0:
                    flag = 1
                    break
            if flag == 0:
                ans.append(i)
        # print(ans)

        return ans
                

        