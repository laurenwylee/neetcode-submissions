class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int l = 0;
        int r = 0;
        HashSet<Character> charSet = new HashSet<>();
        while(r < s.length())
        {
            while(charSet.contains(s.charAt(r)))
            {
                charSet.remove(s.charAt(l));
                l += 1;
            }
            max = Math.max(max, r - l + 1);
            charSet.add(s.charAt(r));
            r += 1;
        }
        return max;
    }
}
