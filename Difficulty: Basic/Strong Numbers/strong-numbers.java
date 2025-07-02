// User function Template for Java

class Solution {
    static int fact(int n){
            if(n==0){
                return 1;
            }
            return n*fact(n-1);
        }
    static int isStrong(int N) {
        // code here
        
        int temp=N;
        int sum=0;
        while(temp>0){
            int r=temp%10;
            sum+=fact(r);
            temp=(int)temp/10;
            
        }
        if(sum==N){
            return 1;
        }
        return 0;
    }
};