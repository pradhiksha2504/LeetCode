class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        i = 0
        while i < n:
            if nums[i] in nums[i+1:]:
                k += 1
                for j in range(nums[i+1:].count(nums[i])):
                    nums.append(nums.pop(i+1))
            i += 1
        return n-k