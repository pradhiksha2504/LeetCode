class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left, right):
            if left >= right:
                return
            
            pivot = nums[randint(left,right)]
            prev, next, curr = left-1, right+1, left
            while curr < next:
                if nums[curr] <pivot:
                    prev += 1
                    nums[prev], nums[curr] = nums[curr], nums[prev]
                    curr += 1
                elif nums[curr] > pivot:
                    next -= 1
                    nums[next], nums[curr] = nums[curr], nums[next]
                else:
                    curr += 1
            quickSort(left, prev)
            quickSort(next, right)
        quickSort(0, len(nums)-1)
        return nums