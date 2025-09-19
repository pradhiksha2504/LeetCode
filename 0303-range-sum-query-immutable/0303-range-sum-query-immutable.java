class NumArray {

    public static int[] prefixSum;
    public NumArray(int[] nums) {
        for(int i =0; i<nums.length; i++){
            if(i-1 >= 0){
                nums[i] += nums[i-1];
            }          
        }
        prefixSum = nums;
    }
    
    public int sumRange(int left, int right) {
        if (left - 1 >= 0){
            return prefixSum[right] - prefixSum[left-1];
        }
        return prefixSum[right];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */