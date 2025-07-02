class Solution {
    // Function to find equilibrium point in the array.
    public static int findEquilibrium(int arr[]) {
        // code here
        int total=0;
        int left=0;
      
        for(int i=0;i<arr.length;i++){
            total+=arr[i];
        }
          int right=total;
        for(int i=0;i<arr.length;i++){
            right-=arr[i];
            if(left==right){
                return i;
                
            }
            left+=arr[i];
        }
        return -1;
    }
}
