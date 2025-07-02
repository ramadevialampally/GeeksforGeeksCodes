// User function Template for Java

class Solution {
    public int binaryToDecimal(String b) {
        // Code here
        int res=0;
        int temp=1;
        for(int i=b.length()-1;i>=0;i--){
            int d=b.charAt(i)-'0';
            res+=temp*d;
            temp*=2;
            
            
        }
        return res;
    }
}