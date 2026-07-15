class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let ret = "";
        for(const s of strs)
        {
            ret += s.length + "#" + s;
        }
        return ret;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 0;
        let ret = [];
        while(i < str.length)
        {
            let j = i;
            while(str[j] != "#")
            {
                j += 1;
            }
            let length = parseInt(str.substring(i, j));
            j = j + 1;
            i = j + length;
            ret.push(str.substring(j, i));
        }
        return ret;
    }
}
