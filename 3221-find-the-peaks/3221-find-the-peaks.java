class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        int l = 1;
        int r = 2;
        int n = mountain.length;
        while(l<n && r <n){
            if(mountain[l]>mountain[r] && mountain[l]> mountain[l-1]){
                res.add(l);
                l++;
                r++;
            }
            else{
                l++;
                r++;
            }

        }
        return res;
        
    }
}