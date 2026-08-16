class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1,2,3
        # 1,2
        A, B = nums1, nums2
        # we want A to be the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(nums1) + len(nums2)
        half = total // 2 # odd totals this rounds down so we'll have to figure it out
        left = 0
        right = len(A)

        while left <= right:
            i = left + (right - left) // 2
            j = half - i
            # Handle index out of bound cases
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')

            if (Aleft <= Bright) and (Bleft <= Aright):
                if total % 2 == 0: # when even, add and divide
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    median = min(Aright, Bright)
                return median
            elif Aleft > Bright: # this means left partition is greater than smallest right partition so we shrink a left
                right = i - 1
            else:
                left = i + 1
