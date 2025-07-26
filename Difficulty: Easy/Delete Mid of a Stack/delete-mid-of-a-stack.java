// User function Template for Java

class Solution {
    // Function to delete middle element of a stack.
    void stack(Stack<Integer> s,int current,int size){
        if(size/2==current){
            s.pop();
            return;
        }
        int tem=s.pop();
        stack(s,current+1,size);
        s.push(tem);
    }
    public void deleteMid(Stack<Integer> s) {
        // code here
        int size=s.size();
        stack(s,0,size);
        
        
    }
}
