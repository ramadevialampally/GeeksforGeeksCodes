class Solution {
    int maxSubarraySum(int[] arr) {
        // Your code here
        int a=Integer.MIN_VALUE;
        int s=0;
        for(int i=0;i<arr.length;i++){
            s+=arr[i];
            if(s>a){
                a=s;
            }
            if(s<0){
                s=0;
            }
        }
        return a;
        
        
    }
}
