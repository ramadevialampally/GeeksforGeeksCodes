// User function Template for Java

class Solution {
    public String is_AutomorphicNumber(int n) {
        // Code here
        int r=n*n;
        if(n%10==r%10){
            return "Automorphic";
        }
        while(n>0){
            if(n%10!=r%10){
                return "Not Automorphic";
            }
            n=n/10;
            r=r/10;
        }
        return "Not Automorphic";
    }
}