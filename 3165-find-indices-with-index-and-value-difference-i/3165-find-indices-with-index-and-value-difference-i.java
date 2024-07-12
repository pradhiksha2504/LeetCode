class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        int[] res = {-1,-1};
        int n = nums.length;
        int l = 0;
        int r = n-1;
        while (l <= r){
            System.out.println("Hello");
            if (Math.abs(nums[l]-nums[r]) >= valueDifference && Math.abs(l-r) >= indexDifference){
                System.out.println("HI");
                res[0]=l;
                res[1]=r;
                return res;
            }
            r --;
            if(l==r){
                l++;
                r = n-1;
            }
        }
        return res;
        
    }
}