class Solution {
    int maxProduct(int[] arr) {
        // code here
        int res=Integer.MIN_VALUE;
        int p=1;
        int s=1;
        for(int i=0;i<arr.length;i++){
            if(p==0) p=1;
            if(s==0) s=1;
            p*=arr[i];
            s*=arr[arr.length-i-1];
            res=Math.max(res,Math.max(p,s));
        }
        return res;
        
    }
}