class Solution {
    int convertfive(int num) {
        // Your code here
        if (num==0){
            return 5;
        }
        if(num<10){
            return num;
        }
        int n=0;
        while(num>0){
            int r=num%10;
            if(r==0){
                n=n*10+5;
            }
            else{
                n=n*10+r;
            }
             num=num/10;
        }
        int res=0;
        while (n>0){
            int r=n%10;
            res=res*10+r;
            n=n/10;
        }
        return res;
       
    }
}