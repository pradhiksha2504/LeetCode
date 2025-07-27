class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        stack = []
        for i in nums:
            if not stack or stack[-1] != i:
                stack.append(i)
        
        for i in range(1, len(stack)-1):
            if stack[i] > stack[i-1] and stack[i] > stack[i+1]:
                count += 1
            elif stack[i] < stack[i-1] and stack[i] < stack[i+1]:
                count += 1
        return count
        