class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f ={}
        ans = []
        n = len(nums)
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        for i, j in f.items():
            if j > (n/3):
                ans.append(i)
        return ans