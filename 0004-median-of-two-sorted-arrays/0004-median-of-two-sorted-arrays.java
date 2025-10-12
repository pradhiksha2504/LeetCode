class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i:nums1){
            arr.add(i);
        }
        for(int i:nums2){
            arr.add(i);
        }
        Collections.sort(arr);
        int n = arr.size();
        if(n% 2==0){
            int mid1 = n/2;
            int mid2 = n/2 - 1;
            return (double)(arr.get(mid1) + arr.get(mid2)) / 2;
        }else{
            return arr.get(n/2);
        }
    }
}