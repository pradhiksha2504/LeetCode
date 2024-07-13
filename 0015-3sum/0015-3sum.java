class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        for(int i=0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int l = i+1;
            int r = n-1;
            while(l<r){
                int x = nums[i]+nums[l]+nums[r];
                if(x==0){
                    List<Integer> ans = new ArrayList<>();
                    ans.add(nums[i]);
                    ans.add(nums[l]);
                    ans.add(nums[r]);
                    result.add(ans);
                    l++;
                    while(nums[l]==nums[l-1] && l<r){
                        l++;
                    }
                }
                else if(x>0){
                    r --;
                }
                else{
                    l++;
                }
            }
            
        }
    return result;
    }
}