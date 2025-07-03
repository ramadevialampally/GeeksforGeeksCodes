// User function Template for Java
class Solution {
    public int findDuplicate(int[] arr) {
        // code here
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<arr.length;i++){
            if(!h.containsKey(arr[i])){
                h.put(arr[i],1);
            }
            else{
                h.put(arr[i],h.get(arr[i])+1);
            }
        }
        for(Map.Entry<Integer, Integer> entry : h.entrySet()){
            if(entry.getValue()>=2){
                return entry.getKey();
            }
        }
        return -1;
    }
}