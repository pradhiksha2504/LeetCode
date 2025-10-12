class Solution {
    public int search(int[] nums, int target) {
        int k = nums[0];
        int rotatedInd = 0;
        int n = nums.length,i=0;
        while(i<n){
            if(nums[i] == target){
                return i;
            }
            if(nums[i] < k && rotatedInd == 0){
                rotatedInd = i ; 
                if(target < k && rotatedInd!=0){
                    i = rotatedInd-1;
                }
            }
            i++;
        }
        return -1;
    }
}