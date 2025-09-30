class Solution {
    public int triangularSum(int[] nums) {
        int res = 0, n = nums.length;

        ArrayList<Integer> newList = new ArrayList<>();
        for(int i:nums){
            newList.add(i);
        }
        int count = n-1;

        while(count > 0){
            ArrayList<Integer> arr = new ArrayList<>();
            for(int i = 0; i < newList.size()-1;i++){
                int sum = (newList.get(i) + newList.get(i+1)) % 10;
                arr.add(sum);
            }
            newList = arr;
            count--;

        }

        return newList.get(0);

        
    }
}