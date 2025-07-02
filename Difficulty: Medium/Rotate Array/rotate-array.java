// User function Template for Java

class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    static void rotateArr(int arr[], int d) {
        // add your code here
        int [] a=new int[arr.length];
        d=d%(arr.length);
        int j=0;
        for(int i=d;i<arr.length;i++){
            a[j]=arr[i];
            j+=1;
            
        }
        for(int i=0;i<d;i++){
            a[j]=arr[i];
            j+=1;
        
        }
        for(int i=0;i<arr.length;i++){
            arr[i]=a[i];
        }
    }
}