// User function Template for Java

class Solution {
    String removeVowels(String s) {
        // code here
         StringBuilder ans = new StringBuilder();
        HashSet<Character> vowels = new HashSet<>();
    vowels.add('a');
    vowels.add('e');
    vowels.add('i');
    vowels.add('o');
    vowels.add('u');
        for(int i=0;i<s.length();i++){
            if(!vowels.contains(s.charAt(i))){
                ans.append(s.charAt(i));
            }
        }
        return ans.toString();
        
    }
}