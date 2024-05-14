class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        f = {}
        for i in range(len(nums)):
            if nums[i] in f and abs(i-f[nums[i]]<=k):
                return True
            f[nums[i]]=i
        # for i in range(len(nums)):
        #     if nums[i] in f:
        #         f[nums[i]].append(i)
        #     else:
        #         f[nums[i]] = [i]
        # for i in f.values():
        #     if len(i)>  1:
        #         j = 1
        #         while j < len(i):
        #             if abs(i[j]-i[j-1]) <= k:
        #                 return True
        #             j +=1


        