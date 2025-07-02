// User function Template for Java

class Solution {
    String removeSpecialCharacter(String s) {
        // code here
        StringBuilder ans=new StringBuilder();
        for(int i=0;i<s.length();i++){
            if(Character.isLetter(s.charAt(i))){
                ans.append(s.charAt(i));
            }
        }
        if(ans.length()==0){
            return "-1";
        }
        return ans.toString();

    }
}