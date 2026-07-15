class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()
        for i, (a, b, c) in enumerate(triplets):
            if target[0] < a or target[1] < b or target[2] < c:
                triplets.pop(i)

        foundA = False
        foundB = False
        foundC = False
        print(triplets)
        for i, (a, b, c) in enumerate(triplets):
            if foundA and foundB and foundC:
                return True
            if a == target[0]:
                foundA = True
            if b == target[1]:
                foundB = True
            if c == target[2]:
                foundC = True

        return foundA and foundB and foundC

