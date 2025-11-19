class Solution {
    public int findFinalValue(int[] nums, int original) {
        while(containsValue(nums, original)){
            original *= 2;
        }
        return original;
        
    }
    private static boolean containsValue(int[] nums, int target){
        for(int n :nums){
            if (n == target){
                return true;
            }
        }
        return false;
    }
}