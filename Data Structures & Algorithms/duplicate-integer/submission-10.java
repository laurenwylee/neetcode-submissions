class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++)
        {
            if(counter.containsKey(nums[i]))
            {
                return true;
            }
            else
            {
                counter.put(nums[i], 1);
            }
        }
        return false;
    }
}