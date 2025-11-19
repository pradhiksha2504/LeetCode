class Solution {
    public int findFinalValue(int[] nums, int original) {
        List<Integer> arr = Arrays.stream(nums).boxed().collect(Collectors.toList());
        while(arr.contains(original)){
            original *= 2;
        }
        return original;
        
    }
}