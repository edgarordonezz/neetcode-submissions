import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force way
        merged = nums1 + nums2
        n = len(merged)
        sort = sorted(merged)

        return statistics.median(merged)