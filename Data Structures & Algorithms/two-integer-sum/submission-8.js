class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let seen = {};
        for(let i = 0; i < nums.length; i++)
        {
            let remainder = target - nums[i];
            if(remainder in seen)
            {
                return [seen[remainder], i];
            }
            seen[nums[i]] = i;
        }
    }
}
