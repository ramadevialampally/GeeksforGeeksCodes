class Solution {
    public ArrayList<Integer> printDivisors(int n) {
        // code here
        ArrayList<Integer> a=new ArrayList<>();
        for(int i=1;i<=n;i++){
            if(n%i==0){
                a.add(i);
            }
        }
        return a;
    }
}