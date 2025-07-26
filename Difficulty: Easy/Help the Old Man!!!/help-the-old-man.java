// User function Template for Java

class Solution {
    static List<List<Integer>> list ;
    static void tower(int N,int src,int aux,int dest){
        if(N==1){
            list.add(Arrays.asList(src,dest));
            return;
        }
        tower(N-1,src,dest,aux);
        list.add(Arrays.asList(src, dest)); 
        tower(N-1,aux,src,dest);
    }
    static List<Integer> shiftPile(int N, int n) {
        // code here
        list = new ArrayList<>();
        int src=1;
        int aux=2;
        int dest=3;
        tower(N,src,aux,dest);
        return list.get(n-1);
        
         
    }
}