class Solution {
    public int subarraySum(int[] nums, int k) {
        int curr = 0, count = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0,1);

        for(int i =0;i<nums.length;i++){
            curr += nums[i];
            int diff = curr - k;
            if(map.containsKey(diff)){
                count += map.get(diff);
            }
            map.put(curr, map.getOrDefault(curr,0)+1);

        }
        return count;
    }
}
