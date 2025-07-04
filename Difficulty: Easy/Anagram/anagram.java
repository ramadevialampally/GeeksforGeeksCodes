class Solution {
    public static boolean areAnagrams(String s1, String s2) {
        // code here
        char[] c1 = s1.toCharArray();
        Arrays.sort(c1);
        char[] c2=s2.toCharArray();
        Arrays.sort(c2);
        return Arrays.equals(c1,c2);
    }
}