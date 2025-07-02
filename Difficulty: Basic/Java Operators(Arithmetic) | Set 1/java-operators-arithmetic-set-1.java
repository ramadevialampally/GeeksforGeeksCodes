
class Solution {
    public double[] FindRoots(int A, int B, int C) {
        // code here
        double[] d=new double[2];
        int res=(B*B)-(4*A*C);
        if(res==0){
            double a=-(B)/(2.0*A);
            d[0]=a;
            d[1]=a;
            
        }
        else if(res>0){
            double a=(-(B)-Math.sqrt(res))/(2.0*A);
            double b=(-(B)+Math.sqrt(res))/(2.0*A);
            d[0]=a;
            d[1]=b;
            
        }
        else{
        return new double[] { -1 };
        }
        Arrays.sort(d);
        return d;
    }
}