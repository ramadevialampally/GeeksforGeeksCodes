// User function Template for Java
class Solution {

    String modify(String s) {
        // your code here
        StringBuilder st=new StringBuilder();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!=' '){
                st.append(s.charAt(i));
            }
        }
        return st.toString();
    }
}