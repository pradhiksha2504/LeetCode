class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in nums and nums.index(x)!=i:
                return [nums.index(x), i]

        