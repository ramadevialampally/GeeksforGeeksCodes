// User function Template for Java

class Solution {
    public boolean isPalindrome(int n) {
        // Code here
        int m=n;
        int res=0;
        while(n>0){
            int r=n%10;
            res=res*10+r;
            n=(int)n/10;
            
        }
        if(m==res){
            return true;
        }
        return false;
        
    }
}