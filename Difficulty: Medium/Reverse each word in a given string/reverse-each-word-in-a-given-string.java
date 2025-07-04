class Solution {
    public String reverseWords(String s) {
        // Code here
        String[] words = s.trim().split("\\s+");
        StringBuilder sb=new StringBuilder();
        for(String i:words){
            StringBuilder in=new StringBuilder(i);
            in.reverse();
            sb.append(in);
            sb.append(" ");
            
        }
        return sb.toString().trim();
        
    }
}
