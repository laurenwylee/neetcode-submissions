class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let freq = {};
        for(let i = 0; i < nums.length; i++)
        {
            if(freq[nums[i]])
            {
                return true;
            }
            freq[nums[i]] = 1;
        }
        return false
    }
}
