class Solution {
    public void rotateclockwise(int[] arr, int k) {
        // code here
       
        k=k%(arr.length);
        int [] a=new int[arr.length];
        int j=0;
        for(int i=arr.length-k;i<arr.length;i++){
            a[j++]=arr[i];
        }
        for(int i=0;i<arr.length-k;i++){
            a[j++]=arr[i];
        }
        for(int i=0;i<arr.length;i++){
            arr[i]=a[i];
        }
        
    }
}