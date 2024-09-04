class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = temp = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                temp += 1
            else:
                temp = 0

            maxlen = max(maxlen, temp)
        return maxlen

        