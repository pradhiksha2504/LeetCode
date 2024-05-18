class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n < 1:
            return nums
        if n == 1:
            return [str(nums[0])]
        ans = [nums[0]]
        for i in range(1, n):
            if nums[i-1]+1 == nums[i]:
                if i == n-1:
                    ans.extend([nums[i],nums[i]])
            else:
                if i == n-1:
                    ans.append(nums[i-1])
                    ans.extend([nums[i],nums[i]])
                else:
                    ans.append(nums[i-1])
                    ans.append(nums[i])
        print(ans)
        res=[]
        i = 0
        while i < len(ans)-1:
            if ans[i]!=ans[i+1]:
                res.append(str(ans[i])+"->"+str(ans[i+1]))
            else:
                res.append(str(ans[i]))
            i+=2
        print(res)
        return res

        