class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        f = Counter(nums)
        ans = []
        for i, j in f.items():
            if j== 2:
                ans.append(i)
                break
        n = len(nums)
        total = (n*(n+1))//2
        ans.append(total - (sum(nums)-ans[0]))
        return ans


        