class Solution {
    static String decToBinary(int n) {
        // code here
        String s="";
        while(n>0){
            int r=n%2;
            s=Integer.toString(r)+s;
            n=n/2;
        }
        return s;
    }
}