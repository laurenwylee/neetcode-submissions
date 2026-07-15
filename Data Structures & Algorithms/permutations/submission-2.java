class Solution {

    public void dfs(int i, List<Integer> curr, List<List<Integer>> result, boolean[] used, int[] nums)
    {
        if(curr.size() == nums.length)
        {
            result.add(new ArrayList<Integer>(curr));
            return;
        }
        for(int j = 0; j < used.length; j++)
        {
            if(used[j] == false)
            {
                curr.add(nums[j]);
                used[j] = true;
                dfs(j, curr, result, used, nums);
                curr.remove(curr.size()-1);
                used[j] = false;
            }
        }
        
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        dfs(0, curr, result, used, nums);
        return result;
    }
}
