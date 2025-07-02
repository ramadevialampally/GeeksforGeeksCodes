class Solution {
    static int gcd(int a,int b){
        while(b!=0){
            int t=b;
            b=a%b;
            a=t;
        }
        return a;
    }
    
    public int lcm(int a, int b) {
        // code here
        return (a*b)/gcd(a,b);
        
    }
}