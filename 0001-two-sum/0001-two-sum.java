class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = {-1,-1};
        if(nums.length < 2){
            return res;
        }
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i:nums){
            arr.add(i);
        }
        
        int ind = 0;

        while(ind < nums.length){
            int diff = target - nums[ind];
            if(arr.contains(diff)){
                int val = arr.indexOf(diff);
                if(val != ind){
                    res[0] = ind;
                    res[1] = arr.indexOf(diff);
                    break;
                }
            }
            ind++;
        }
        
        return res;

    }
}