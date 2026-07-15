class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length)
        {
            return false;
        }
        let freq = {};
        for(let i = 0; i < s.length; i++)
        {
            freq[s[i]] = 1 + (freq[s[i]] || 0);
        }
        for(let i = 0; i < t.length; i++)
        {
            if(!freq[t[i]])
            {
                return false;
            }
            freq[t[i]] -= 1;
        }
        return true;
    }
}
