class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        curr = 0
        for n in nums:
            curr += n
            self.arr.append(curr)
        

    def sumRange(self, left: int, right: int) -> int:
        rsum = self.arr[right]
        lsum = self.arr[left-1] if left > 0 else 0
        return rsum - lsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)