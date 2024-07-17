class Solution {
    public boolean isPalindrome(int x) {
        int y = x;
        int sum = 0;
        while(x>0){
            int a = x%10;
            sum = (sum*10) + a;
            x /= 10;
        }
        if(sum == y){
            return true;
        }
        else{
            return false;
        }
        
    }
}