class Solution {
    public int maxSubArray(int[] nums) {
        int mini = 0;
        int maxi = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            mini = mini+nums[i];
            maxi = Math.max(maxi,mini);
            if (mini<0){
                mini = 0;
            }   
        }
        return maxi;
    }
}