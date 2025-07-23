class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        currsum, maxsum = 0, 0
        visited = set()

        for right in range(len(nums)):
            while nums[right] in visited:
                currsum -= nums[left]
                visited.remove(nums[left])
                left += 1
            currsum += nums[right]
            visited.add(nums[right])
            right += 1
            maxsum = max(currsum, maxsum)
        return maxsum
        