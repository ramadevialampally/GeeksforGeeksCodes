// User function Template for Java
class Solution {
    static boolean armstrongNumber(int n) {
        // code here
        int res=0;
        int temp=n;
        while(n>0){
            int r=n%10;
            res+=(r*r*r);
            n=(int)n/10;
        }
        if(res==temp){
            return true;
        }
        return false;
    }
}