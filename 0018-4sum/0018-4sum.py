class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n-2):
                l = j+1
                r = n-1
                while l<r:
                    x = nums[i]+nums[j]+nums[l]+nums[r]
                    if x == target:
                        y = sorted([nums[i],nums[j],nums[r],nums[l]])
                        if i!=j!=r!=l and y not in ans:
                            ans.append(y)
                    if x > target:
                        r-=1
                    else:
                        l+=1
        return ans