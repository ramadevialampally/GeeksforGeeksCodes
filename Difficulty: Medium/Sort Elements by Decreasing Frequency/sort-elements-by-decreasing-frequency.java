// User function Template for Java

class Solution {
    // Function to sort the array according to frequency of elements.
    public ArrayList<Integer> sortByFreq(int arr[]) {
        // add your code here
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<arr.length;i++){
            if(!h.containsKey(arr[i])){
                h.put(arr[i],1);
            }
            else{
                h.put(arr[i],h.get(arr[i])+1);
            }
        }
         List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(h.entrySet());

    // Step 3: Sort by frequency descending, then key ascending
    entryList.sort((a, b) -> {
        if (!b.getValue().equals(a.getValue())) {
            return b.getValue() - a.getValue(); // Descending frequency
        } else {
            return a.getKey() - b.getKey();     // Ascending key if tie
        }
    });
    ArrayList<Integer> a=new ArrayList<>();
    for (Map.Entry<Integer, Integer> entry : entryList){
        for(int i=0;i<entry.getValue();i++){
            a.add(entry.getKey());
        }
    }
    return a;
    }
}