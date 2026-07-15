class Solution {
    public void dfs(int i, int currSum, List<List<Integer>> result, List<Integer> curr, int target, int[] candidates)
    {
        if(currSum == target)
        {
            result.add(new ArrayList<Integer>(curr));
            return;
        }
        if(i == candidates.length || currSum > target)
        {
            return;
        }

        curr.add(candidates[i]);
        currSum += candidates[i];
        dfs(i+1, currSum, result, curr, target, candidates);

        curr.remove(curr.size()-1);
        currSum -= candidates[i];
        int j = i + 1;
        while (j < candidates.length && candidates[j] == candidates[i])
        {
            j++;
        }
        if(j < candidates.length)
        {
            dfs(j, currSum, result, curr, target, candidates);
        }

    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        int currSum = 0;

        dfs(0, currSum, result, curr, target, candidates);
        return result;
    }
}
