// User function Template for Java

class Solution {
    String removeDuplicates(String s) {
        StringBuilder sb=new StringBuilder();
        Set<Character> se=new HashSet<>();
        for(int i=0;i<s.length();i++){
            if(! se.contains(s.charAt(i))){
                se.add(s.charAt(i));
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
