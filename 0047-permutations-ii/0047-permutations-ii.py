from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        p = permutations(nums)
        ans = []
        for i in p:
            if list(i) not in ans:
                ans.append(list(i))
        return ans