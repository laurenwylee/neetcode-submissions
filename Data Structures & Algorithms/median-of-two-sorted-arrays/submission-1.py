class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        k = (total) // 2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        def binSearch(l, r):
            mid1 = l + (r - l) // 2
            mid2 = k - mid1
            left1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            right1 = float("inf") if mid1 == len(nums1) else nums1[mid1]

            left2 = float("-inf") if mid2 == 0 else nums2[mid2 - 1]
            right2 = float("inf") if mid2 == len(nums2) else nums2[mid2]


            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            if left1 > right2:
                r = mid1 - 1
            elif left2 > right1:
                l = mid1 + 1

            return binSearch(l, r)
        return binSearch(0, len(nums1))