class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2
            j = half - i

            leftA = A[i - 1] if i > 0 else float("-inf")
            rightA = A[i] if i < len(A) else float("inf")

            leftB = B[j - 1] if j > 0 else float("-inf")
            rightB = B[j] if j < len(B) else float("inf")

            # Partition is too far right in A
            if leftA > rightB:
                r = i - 1

            # Partition is too far left in A
            elif leftB > rightA:
                l = i + 1

            # Correct partition
            else:
                if total % 2:
                    return max(leftA, leftB)

                return (max(leftA, leftB) + min(rightA, rightB)) / 2