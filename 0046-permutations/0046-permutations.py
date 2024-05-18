from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = permutations(nums)
        ans = []
        for i in p:
            ans.append(list(i))
        return ans
        