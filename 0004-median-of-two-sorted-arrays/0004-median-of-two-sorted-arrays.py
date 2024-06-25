class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        big= nums1+nums2
        big.sort()   
        median = float()
        n = len(big)
        if n%2==0:
            median = (big[(n//2)-1]+(big[n//2]))/2.0
        else:
            median = big[n//2]
        return median