class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let anagrams = {};
        for(let s of strs)
        {
            let count = new Array(26).fill(0);
            for(let c of s)
            {
                count[c.charCodeAt(0) - "a".charCodeAt(0)] += 1;
            }
            if(!anagrams[count])
            {
                anagrams[count] = [];
            }
            anagrams[count].push(s);
        }
        return Object.values(anagrams);
    }
}
