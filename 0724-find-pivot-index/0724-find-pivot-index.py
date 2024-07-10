class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i,x in enumerate(nums):
            right -= x
            if left == right:
                return  i
            left += x
        return -1


        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1

        