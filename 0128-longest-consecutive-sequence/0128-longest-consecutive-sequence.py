class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0
        for i in nums:
            if i-1 not in numSet:
                length = 1
                while i+length in numSet:
                    length += 1
                count = max(length, count)
        return count