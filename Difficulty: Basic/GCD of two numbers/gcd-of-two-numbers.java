class Solution {
    public static int gcd(int a, int b) {
        // code here
        while(b!=0){
            int t=b;
            b=a%b;
            a=t;
        }
        return a;
    }
}
