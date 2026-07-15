class Solution {

    public void dfs(int i, ArrayList<Integer> lst, int[] nums, List<List<Integer>> acc)
    {
        if(i == nums.length)
        {
            acc.add(new ArrayList<Integer>(lst));
            return;
        }
        lst.add(nums[i]);
        dfs(i+1, lst, nums, acc);
        lst.remove(lst.size() - 1);
        dfs(i+1, lst, nums, acc);
        
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        ArrayList<Integer> lst = new ArrayList<Integer>();
        dfs(0, lst, nums, ret);
        return ret;

    }
}
