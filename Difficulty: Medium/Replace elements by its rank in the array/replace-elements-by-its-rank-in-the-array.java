// User function Template for Java

class Solution {
    static int[] replaceWithRank(int arr[], int N) {
        // code here
        HashMap<Integer,Integer> h=new HashMap<>();
        int m[]=Arrays.copyOf(arr, arr.length);
        Arrays.sort(m);
        int k=1;
        for(int i=0;i<m.length;i++){
            if(!(h.containsKey(m[i]))){
                h.put(m[i],k++);
            }
            
        }
        for(int i=0;i<arr.length;i++){
            arr[i]=h.get(arr[i]);
        }
        return arr;
    
    }
}
