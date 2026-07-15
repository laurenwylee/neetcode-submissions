class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        for(int stone: stones)
        {
            maxHeap.add(stone);
        }
        while(maxHeap.size() != 0)
        {
            if(maxHeap.size() == 1)
            {
                return maxHeap.poll();
            } else
            {
                int x = maxHeap.poll();
                int y = maxHeap.poll();
                maxHeap.add(x - y);
            }
        }
        return 0;
    }
}
