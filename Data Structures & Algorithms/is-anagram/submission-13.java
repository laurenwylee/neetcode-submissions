class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
        {
            return false;
        }
        HashMap<Character, Integer> sCounter = new HashMap<>();
        HashMap<Character, Integer> tCounter = new HashMap<>();
        for(int i = 0; i < s.length(); i++)
        {
            if(sCounter.containsKey(s.charAt(i)))
            {
                sCounter.put(s.charAt(i), sCounter.get(s.charAt(i)) + 1);
            }
            else
            {
                sCounter.put(s.charAt(i), 1);
            }
        }
        for(int i = 0; i < t.length(); i++)
        {
            if(tCounter.containsKey(t.charAt(i)))
            {
                tCounter.put(t.charAt(i), tCounter.get(t.charAt(i)) + 1);
            }
            else
            {
                tCounter.put(t.charAt(i), 1);
            }
        }
        return sCounter.equals(tCounter);
    }
}
