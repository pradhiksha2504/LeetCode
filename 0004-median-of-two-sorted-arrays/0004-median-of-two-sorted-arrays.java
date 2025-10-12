class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Integer> arr = new ArrayList<>();
        int left = 0,right = 0;
        while(left < nums1.length && right < nums2.length){
            if(nums1[left] < nums2[right]){
                arr.add(nums1[left++]);
            }else if(nums1[left] > nums2[right]){
                arr.add(nums2[right++]);
            }else{
                arr.add(nums1[left++]);
                arr.add(nums2[right++]);
            }
        }
        while(left < nums1.length){
            arr.add(nums1[left++]);
        }
        while(right < nums2.length){
            arr.add(nums2[right++]);
        }
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