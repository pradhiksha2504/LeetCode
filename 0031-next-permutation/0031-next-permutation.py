class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        k = n - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        if k == -1:
            nums.reverse()
            return
        l = n - 1
        while l > k and nums[k] >= nums[l]:
            l -= 1
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = reversed(nums[k + 1:])

