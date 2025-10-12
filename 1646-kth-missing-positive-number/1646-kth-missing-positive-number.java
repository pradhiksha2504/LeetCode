class Solution {
    public int findKthPositive(int[] arr, int k) {
        int count = 0;
        int num = 1, lastElement = arr[arr.length-1];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] != num){
                count = count + arr[i]-num;
                if(count == k){
                    return (arr[i]-k) + k - 1;
                }
                if(count > k){
                    lastElement = arr[i];
                    break;
                }
                num = arr[i];
            }
            num++;
        }
        if(count > k){
            return lastElement - (count-k) - 1;
        }
        else if(count == 0){
            return lastElement +k;
        }
        else{
            return lastElement + k- count;
        }
        
    }
}