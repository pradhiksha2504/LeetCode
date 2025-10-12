class Solution {
    public int climbStairs(int n) {
        if(n < 2){
            return n;
        }
        int i = 1, n1 = 0, n2 = 1;
        int n3 = n1 + n2;
        while(i < n){
            n1 = n2;
            n2 = n3;
            n3 = n1+n2;
            i++;
        }
        return n3;

    }
}