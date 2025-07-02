
class Solution {
    public boolean isSubset(int a[], int b[]) {
        // Your code here
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<a.length;i++){
            if(! h.containsKey(a[i])){
                h.put(a[i],1);
            }
            else{
                h.put(a[i],h.get(a[i])+1);
            }
        }
        for(int i=0;i<b.length;i++){
            if(! h.containsKey(b[i]) || h.get(b[i])==0){
                return false;
            }
            else{
                h.put(b[i],h.get(b[i])-1);
            }
        }
        return true;
        
    }
}
