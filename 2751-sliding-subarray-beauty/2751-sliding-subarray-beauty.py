from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        first = SortedList()
        for i in range(k):
            first.add(nums[i])
        res = []
        n = len(nums)
        ind = x-1
        for i in range(n-k+1):
            if first[ind] < 0:
                res.append(first[ind])
            else:
                res.append(0)
            first.discard(nums[i])
            if i+k==n:
                first.add(nums[n-1])
            else:
                first.add(nums[i+k])
            # first.sort()
        return res
        
        