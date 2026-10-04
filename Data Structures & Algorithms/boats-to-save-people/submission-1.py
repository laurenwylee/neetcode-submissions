class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            if r == l:
                count += 1
                break
            weight = people[l] + people[r]
            if weight <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                count += 1
                r -= 1
        return count