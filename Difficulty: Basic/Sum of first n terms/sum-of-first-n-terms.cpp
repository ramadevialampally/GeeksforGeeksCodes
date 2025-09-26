// User function template for C++

class Solution {
  public:
    int sumOfSeries(int n) {
        // code here
        int sum =0,i;
        for(i=1;i<=n;i++){
            sum=sum+(i*i*i);
        }
        return sum;
    }
};