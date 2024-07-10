class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int x = 0;
        int y = 1;
        int z = 2;
        int n = arr.length;
        while(x<n & y<n & z<n){
            if(arr[x]%2 != 0){
                if(arr[y]%2 != 0){
                    if(arr[z]%2!=0){
                        return true;
                    }
                }
            }
            x++;
            y++;
            z++;
        }
        return false;  
    }
}