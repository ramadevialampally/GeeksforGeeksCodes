// User function Template for Java

class Solution {
    public long sum_of_gp(long n, long a, long r) {
        // Code here
        long sum=0;
        for(int i=0;i<n;i++){
            sum+=a;
            a=a*r;
        }
        return sum;
    }
}