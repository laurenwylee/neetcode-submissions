class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for x in nums:
            if x in counter.keys():
                counter[x] += 1
            else:
                counter[x] = 1
        counter = sorted(counter.items(), key = lambda item: item[1])
        print(counter)
        ret_val = []
        for x in range(k):
            ret_val.append(counter[len(counter) - 1 - x][0])
        return ret_val