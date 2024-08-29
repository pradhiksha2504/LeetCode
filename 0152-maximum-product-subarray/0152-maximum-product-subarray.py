class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = max(nums)
        for i in nums:
            if i == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * i
            curMax = max(temp, i*curMin, i)
            curMin= min(temp, i*curMin, i)
            res = max(res, curMax, curMin)
        return res
        