class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        f = {}
        for i in range(len(nums)):
            if nums[i] in f:
                f[nums[i]].append(i)
            else:
                f[nums[i]] = [i]
        print(f)
        ans = []
        for i in f.values():
            if len(i)>  1:
                mini = i[0]
                temp = mini
                j = 1
                while j < len(i):
                    if abs(i[j]-i[j-1]) <= k:
                        print(i[j],i[j-1])
                        return True
                    j +=1


        