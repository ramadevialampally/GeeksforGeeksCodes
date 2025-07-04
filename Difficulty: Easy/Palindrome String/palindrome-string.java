class Solution {
    boolean isPalindrome(String s) {
        // code here
        
        StringBuilder sbb=new StringBuilder(s).reverse();
        return sbb.toString().equals(s);
    }
}