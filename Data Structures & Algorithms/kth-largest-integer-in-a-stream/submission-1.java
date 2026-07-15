class KthLargest {

    private PriorityQueue<Integer> minHeap;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++)
        {
            this.minHeap.add(nums[i]);
        }

    }
    
    public int add(int val) {
        this.minHeap.add(val);
        while(this.minHeap.size() > k)
        {
            minHeap.remove();
        }
        return minHeap.peek();
    }
}
