class Solution {

    public void dfs(int i, int currSum, List<List<Integer>> result, List<Integer> combo, int[] nums, int target)
    {
        if(i == nums.length && currSum == target)
        {
            result.add(new ArrayList<Integer>(combo));
            return;
        }
        if(currSum > target || i == nums.length)
        {
            return;
        }

        currSum = nums[i] + currSum;
        combo.add(nums[i]);
        dfs(i, currSum, result, combo, nums, target);
        currSum -= nums[i];
        combo.remove(combo.size()-1);
        dfs(i + 1, currSum, result, combo, nums, target);
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> combo = new ArrayList<>();
        dfs(0, 0, result, combo, nums, target);
        return result;
    }
}
