class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                ans[x] = i - x
            stack.append(i)
        return ans
