class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        count = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            freq[n] += 1
        for n, f in freq.items():
            count[f].append(n)

        print(freq)
        res = []
        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res