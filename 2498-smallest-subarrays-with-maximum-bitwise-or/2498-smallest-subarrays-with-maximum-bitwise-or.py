from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        last_seen = [-1] * 32  # tracks the last index where each bit is seen
        answer = [1] * n  # initialize all subarray lengths to 1

        for i in range(n - 1, -1, -1):  # right to left
            for bit in range(32):
                if (nums[i] >> bit) & 1:
                    last_seen[bit] = i  # update last seen for this bit
            
            # max_index = the farthest index we need to reach to include all OR bits
            max_index = i
            for bit in range(32):
                if last_seen[bit] != -1:
                    max_index = max(max_index, last_seen[bit])
            
            answer[i] = max_index - i + 1
        
        return answer
