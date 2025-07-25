class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        f = {}
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        arr = list(f.keys())
        res = max(arr)
        for i in arr:
            if i >= 0 and i != max(arr):
                res += i
        return res
        